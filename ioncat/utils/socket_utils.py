import socket
import socks
import ssl

DEFAULT_PORTS = {
    "http": 80, 
    "https": 443,
    "ftp": 21,
    "ssh": 22,
    "telnet": 23,   
    "smtp": 25,
    "dns": 53,
    "dhcp": 67,
    "tftp": 69,
    "http-alt": 8080,
    "https-alt": 8443,
    "smb": 445,
    "mssql": 1433,
    "mysql": 3306,
    "postgresql": 5432,
    "rdp": 3389,
    "vnc": 5900,
    "snmp": 161,
    "snmp-trap": 162,
    "netbios-ns": 137,
    "netbios-dgm": 138,
    "netbios-ssn": 139,
    "ldap": 389,    
    "ldaps": 636,
    "mongodb": 27017,
    "redis": 6379,
    "memcached": 11211,
    "zookeeper": 2181,
    "kafka": 9092,
    "rabbitmq": 5672,
    "cassandra": 9042,
    "couchdb": 5984,
    "elasticsearch": 9200,
    "kibana": 5601,
    "grafana": 3000,    
    "prometheus": 9090,
    "minecraft": 25565,
    "gtp": 2123,
    "samp": 7777,
    "teamspeak": 9987,
    "ventrilo": 3784,   
    "mumble": 64738,
    "fivem": 30120,
    None: None
}

def default_protocol_port(protocol: str):
    return DEFAULT_PORTS[protocol]

def parse_target(target: str):
    protocol = None
    host = None
    port = None
    path = "/"
    
    if "://" in target: 
        protocol, target = target.split("://")
    
    if "/" in target:
        target, path = target.split("/", 1)
        
    if ":" in target:
        host, port = target.split(":")
        port = int(port)
    else:
        host = target
        port = default_protocol_port(protocol)
    
    if not port:
        raise ValueError(f"Cannot determine port for protocol: {protocol}\n\t\tPlease specify a port manually or use a valid protocol (like http://, https://)") 
    
    # Return as json
    return {
        "protocol": protocol,
        "host": host,
        "port": port,
        "path": path
    }

def create_raw_socket(tcp: bool, proxy: None | str):
    if proxy:
        proxy_type, proxy_host, proxy_port = proxy.split(":")
        proxy_port = int(proxy_port)
        
        if tcp:
            s = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            s = socks.socksocket(socket.AF_INET, socket.SOCK_DGRAM)
        
        s.set_proxy(socks.PROXY_TYPES[proxy_type.upper()], proxy_host, proxy_port)
        return s
    else:
        if tcp:
            return socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            return socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    

def create_tcp(raw_target: str, proxy: None | str):
    s = create_raw_socket(True, proxy)
    s.settimeout(5)
    
    target = parse_target(raw_target)
    protocol = target["protocol"]
    host = target["host"]
    port = target["port"]
    
    if protocol == "https":
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        s = ctx.wrap_socket(s, server_hostname=host)
    
    s.connect((host, port))
    return s

def create_udp(raw_target: str, proxy: None | str):
    s = create_raw_socket(False, proxy)
    s.settimeout(5)
    
    target = parse_target(raw_target)
    host = target["host"]
    port = target["port"]
    
    s.connect((host, port))
    return s