import sys
import click
from colorama import Fore

import logger

from modules.fastclose import async_run_fast_close
from modules.http import async_run_http
from modules.slowloris import async_run_slowloris

from utils.proxy_parser import load_proxies
from utils.ua_parser import load_uas
from utils.os_utils import get_vcores

VCORES_COUNT = get_vcores()

def print_banner():
    print(Fore.CYAN + """
      ／1、             
    （ﾟ､ ｡ ７       IonCAT: Multi layered network I/O stress tool.
      |   ヽ           Wanna stress som nets today? -w- prrr...
      じし_,)ノ
    """)

@click.group()
@click.option("--headless", default=False, is_flag=True, help="Headless mode (No colors and formatting)")
@click.option("--proxies", default="data/proxies.txt", help="File with proxies to use")
@click.option("--unsafe", default=False, is_flag=True, help="Run without proxies")
def main(headless: bool, proxies: str, unsafe: bool):
    logger.init_logger(headless)
    load_proxies(proxies, unsafe)
    
@main.command()
@click.argument("target", required=True, type=str)
@click.option("--method", "-m", default="GET", help="HTTP Method to use (GET/POST)")
@click.option("--threads", "-t", default=VCORES_COUNT, help="Threads count to use")
@click.option("--uas", default="data/user-agents.txt", help="User-Agents file to use")
def fastclose(target: str, method: str, threads: int, uas: str):
    load_uas(uas)
    async_run_fast_close(threads, target, method)

@main.command()
@click.argument("target", required=True, type=str)
@click.option("--bypass", "-b", default=False, is_flag=True, help="Mimics a real browser and bypass WAFs")
@click.option("--method", "-m", default="GET", help="HTTP Method to use (GET/POST)")
@click.option("--random-body", "-r", default=False, is_flag=True, help="Randomize request body")
@click.option("--threads", "-t", default=VCORES_COUNT, help="Threads count to use")
@click.option("--uas", default="data/user-agents.txt", help="User-Agents file to use")
def http(target: str, bypass: bool, method: str, random_body: bool, threads: int, uas: str):
    load_uas(uas)
    async_run_http(threads, target, bypass, method, random_body)

@main.command()
@click.argument("target", required=True, type=str)
@click.option("--bypass", "-b", default=False, is_flag=True, help="Mimics a real browser and bypass WAFs")
@click.option("--method", "-m", default="GET", help="HTTP Method to use (GET/POST)")
@click.option("--sockets", "-s", default=64, help="Simultaneous sockets to use")
@click.option("--threads", "-t", default=VCORES_COUNT, help="Threads count to use")
def slowloris(target: str, bypass: bool, method: str, sockets: int, threads: int):
    async_run_slowloris(threads, target, bypass, method, sockets)

def start():
    args = sys.argv[1:]
    headless = False
    
    for _, arg in enumerate(args):
        if arg == "--headless":
            headless = True
            
    if not headless:
        print_banner()
    
    try:
        main()
        exit(0)
    except Exception as e:
        logger.err(f"Error: {e}")
        exit(1)