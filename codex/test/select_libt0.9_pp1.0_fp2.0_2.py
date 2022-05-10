import selectors
import sys
import logging


logging.basicConfig(level=logging.INFO, format="%(message)s")
# Replace hèredoc with json module
request_html = """\
GET {path} HTTP/1.1\r\nHost: localhost\r\n\r\n\
"""

def fetch_html(path):
    sock = socket.socket()
    sock.connect(("localhost", 3000))

    request = request_html.format(path=path)
    sock.send(request.encode("ascii"))

    chunks = []

    while True:
        chunk = sock.recv(4096)
        logging.info("Received chunk")
        if chunk:
            chunks.append(chunk)
        else:
            break
    return b"".join(chunks).decode("utf-8")


class SelectorEventLoop:
    def __init__(self):
        self.selector = selectors.DefaultSelector()

