import random
import socket

# Random accept headers that mimic a real browser.
ACCEPT_HEADERS = [
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,application/json",
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
]

# Random accept encoding headers that mimic a real browser.
ACCEPT_ENCODING_HEADERS = [
    "gzip, deflate, br",
    "gzip, deflate",
    "gzip, deflate, sdch",
    "gzip, deflate, sdch, br",
    "gzip, deflate, sdch, br, x-gzip",
]

# Random accept language headers that mimic a real browser.
ACCEPT_LANGUAGE_HEADERS = [
    "en-US,en;q=0.9",
    "es-419,es;q=0.9",
    "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
    "fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5",
    "de-CH",
    "es-MX,es,en",
    "en-UK, en, de;q=0.5",
    "en-US,fr-CA",
    "*"
]

# Random device memory headers that mimic a real browser.
DEVICE_MEMORY_HEADERS = [
    "8",
    "4",
    "2",
    "1",
    "0.5",
    "0.25",
]

# Random ECT headers that mimic a real browser.
ECT_HEADERS = [
    "5g",
    "4g",
    "3g",
    "2g",
    "slow-2g",
]

# Random referer headers that mimic a real browser.
REFERER_HEADERS = [
    "https://www.google.com/",
    "https://www.bing.com/",
    "https://www.yahoo.com/",
    "https://www.duckduckgo.com/",
    "https://www.ecosia.org/",
    "https://www.ask.com/",
    "https://www.aol.com/",
    "https://www.webcrawler.com/",
    "https://www.dogpile.com/",
    "https://www.yandex.com/",
    "https://www.baidu.com/",
    "https://www.naver.com/",
    "https://www.daum.net/",
    "https://www.sogou.com/",
    "https://www.seznam.cz/",
    "https://www.qwant.com/",
    "https://www.yippy.com/",
    "https://www.startpage.com/",
    "https://www.ixquick.com/",
    "https://www.mojeek.com/",
    "https://www.gibiru.com/",
    "https://www.searchencrypt.com/",
    "https://www.search.com/",
]

# Random SEC-CH-PREFERS-COLOR-SCHEME headers that mimic a real browser.
SEC_CH_PREFERS_COLOR_SCHEME_HEADERS = [
    "dark",
    "light",
]

# Random SEC-CH-PREFERS-REDUCED-MOTION headers that mimic a real browser.   
SEC_CH_PREFERS_REDUCED_MOTION_HEADERS = [
    "no-preference",
    "reduce",
]

# Random SEC-CH-UA headers that mimic a real browser.
SEC_CH_UA_HEADERS = [
    "Chromium;v=92, Not A;Brand;v=99, Google Chrome;v=92",
    "Chromium;v=92, Not A;Brand;v=99, Microsoft Edge;v=92",
    "Chromium;v=92, Not A;Brand;v=99, Opera;v=92",
    "Gecko;v=92",
    "AppleWebKit;v=92",
    "Mozilla;v=92",
]

# Random SEC-CH-UA-ARCH headers that mimic a real browser.
SEC_CH_UA_ARCH_HEADERS = [
    "x64",
    "x86",
]

# Random SEC-CH-UA-FULL-VERSION headers that mimic a real browser.
SEC_CH_UA_FULL_VERSION_HEADERS = [
    "92.0.4515.159",
    "92.0.4515.131",
    "92.0.4515.107",
    "92.0.4515.101",
    "92.0.4515.105",
    "92.0.4515.104",
    "92.0.4515.103",
    "92.0.4515.102",
    "92.0.4515.101",
    "92.0.4515.100",
]

# Random SEC-CH-UA-PLATFORM headers that mimic a real browser.  
SEC_CH_UA_PLATFORM_HEADERS = [
    "Windows",
    "Linux",
    "Mac",
    "Android",
    "iOS",
    "iPad",
    "iPhone",
    "iPod",
]

# Random SEC-CH-UA-PLATFORM-VERSION headers that mimic a real browser.
SEC_CH_UA_PLATFORM_VERSION_HEADERS = [
    "10",
    "8.1",
    "8",
    "7",
    "6.3",
    "6.2",
    "6.1",
    "6.0",
    "5.1",
    "5.0",
    "4.0",
    "3.1",
    "3.0",
    "2.0",
    "1.0",
]

# Random SEC-FETCH-DEST headers that mimic a real browser.  
SEC_FETCH_DEST_HEADERS = [
    "document",
    "embed",
    "font",
    "image",
    "manifest",
    "media",
    "object",
    "report",
    "script",
    "serviceworker",
    "sharedworker",
    "style",
    "worker",
    "xslt",
]

# Random SEC-FETCH-MODE headers that mimic a real browser.
SEC_FETCH_MODE_HEADERS = [
    "navigate",
    "nested-navigate",
    "same-origin",
]

# Random VIEWPORT-WIDTH headers that mimic a real browser.
VIEWPORT_WIDTH_HEADERS = [
    "1920",
    "1280",
    "1024",
    "768",
    "640",
    "320",
]

BROWSER_TYPE = ["chrome", "firefox"]

def generate_id():
    return "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", k=6))

class HTTPMimic:
    def __init__(self, s: socket.socket, bypass: bool):
        self.s = s
        self.bypass = bypass
        self.type = random.choice(BROWSER_TYPE)
        self.id = generate_id()
        
    def send(self, data: str):
        line = f"{data}\r\n"
        self.s.send(line.encode("utf-8"))
        
    def send_version(self, method: str, path: str):
        text = f"{method} {path} HTTP/1.1"
        self.send(text) 
        
    def send_header(self, key: str, value: str):
        text = f"{key}: {value}"
        self.send(text)
        
    def send_headers(self, host: str):
        self.send_header("Host", host)
        if not self.bypass:
            return
        
        self.send_header("Accept", random.choice(ACCEPT_HEADERS))
        self.send_header("Accept-Encoding", random.choice(ACCEPT_ENCODING_HEADERS)) 
        self.send_header("Accept-Language", random.choice(ACCEPT_LANGUAGE_HEADERS))
        self.send_header("Device-Memory", random.choice(DEVICE_MEMORY_HEADERS))
        self.send_header("ECT", random.choice(ECT_HEADERS))
        self.send_header("Referer", random.choice(REFERER_HEADERS))
        self.send_header("Viewport-Width", random.choice(VIEWPORT_WIDTH_HEADERS))
        
        if self.type == "chrome":
            self.send_header("Sec-Ch-Prefers-Color-Scheme", random.choice(SEC_CH_PREFERS_COLOR_SCHEME_HEADERS))
            self.send_header("Sec-Ch-Prefers-Reduced-Motion", random.choice(SEC_CH_PREFERS_REDUCED_MOTION_HEADERS)) 
            self.send_header("Sec-Ch-UA", random.choice(SEC_CH_UA_HEADERS))
            self.send_header("Sec-Ch-UA-Arch", random.choice(SEC_CH_UA_ARCH_HEADERS))
            self.send_header("Sec-Ch-UA-Full-Version", random.choice(SEC_CH_UA_FULL_VERSION_HEADERS))
            self.send_header("Sec-Ch-UA-Platform", random.choice(SEC_CH_UA_PLATFORM_HEADERS))
            self.send_header("Sec-Ch-UA-Platform-Version", random.choice(SEC_CH_UA_PLATFORM_VERSION_HEADERS))
            self.send_header("Sec-Fetch-Dest", random.choice(SEC_FETCH_DEST_HEADERS))
            self.send_header("Sec-Fetch-Mode", random.choice(SEC_FETCH_MODE_HEADERS))
            
    def flush(self):
        self.send("")
        
    def end(self):
        self.s.close()
            
    def send_body(self, body: str):
        self.send_header("Content-Length", str(len(body)))
        self.flush()
        self.send(body)
        
    def recv(self, size: int):
        return self.s.recv(size)