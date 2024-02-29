import logger
import random

PROXIES = []    

# Load proxies from file
def load_proxies(path: str, unsafe: bool):
    # Check if file exist.
    try:
        with open(path, "r") as f:
            # Read file
            data = f.read() 
            # Parse file
            lines = data.split("\n")
            # Iterate over lines
            for line in lines:
                # Check if line is not empty
                if line and not line.strip().startswith("#"):
                    parts = line.split(":")
                    if len(parts) != 2:
                        logger.warn(f"Invalid proxy format: {line}")
                        continue
                    
                    # Append line to PROXIES
                    if parts[0] in ["http", "socks4", "socks5"]:
                        PROXIES.append(line)
                    else:
                        print(f"Invalid proxy type: {line.split(':')[0]}, use http, socks4 or socks5")
                        continue
                    
        if is_proxy_loaded():
            logger.info(f"Loaded {len(PROXIES)} proxies from {path}")
        elif unsafe:
            logger.warn(f"No proxies loaded from {path} (File is empty)")
            logger.warn("Running without proxies (unsafe mode)")
        else:
            logger.warn(f"No proxies loaded from {path} (File is empty)")
            logger.err("If you want to run without proxies, use --unsafe flag before command. Otherwise, specify a valid file using --proxies flag.")
            exit(1) 
    except FileNotFoundError:
        if unsafe:
            logger.warn(f"File not found: {path}")
            logger.warn("Running without proxies (unsafe mode)")
        else:
            logger.err(f"File not found: {path}")
            logger.err("If you want to run without proxies, use --unsafe flag before command. Otherwise, specify a valid file using --proxies flag.")
            exit(1)
                
def is_proxy_loaded():
    return len(PROXIES) > 0
                
# Return random proxy
def get_random_proxy():
    if not is_proxy_loaded():
        return None
    
    return random.choice(PROXIES)