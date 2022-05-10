import selectors
import sys
import traceback

from http import HTTPStatus
from io import BytesIO

sel = selectors.DefaultSelector()


def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print("accepted connection from", addr)
    conn.setblocking(False)
    message = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=message)


def service_connection(key, mask):
    sock = key.fileobj
    message = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            message.outb += recv_data
        else:
            print("closing connection to", message.addr)
            sel.unregister(sock)
            sock.close()

