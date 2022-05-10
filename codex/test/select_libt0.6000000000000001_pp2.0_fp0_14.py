import selectors
import time
import json
import logging
import sys

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s,%(msecs)d %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
    stream=sys.stderr,
)

HOST = "127.0.0.1"
PORT = 65432

sel = selectors.DefaultSelector()
messages = [
    b"Message 1 from client.",
    b"Message 2 from client.",
]

def start_connections(host, port, num_conns):
    server_addr = (host, port)
    for i in range(0, num_conns):
        connid = i + 1
        logging.debug("starting connection", connid, "to", server_addr)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
