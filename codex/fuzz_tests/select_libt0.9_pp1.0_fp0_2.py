import selectors
import socketserver
import threading
import re

HOST, PORT = "localhost", 9999
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
        if not recv_data:
            print('closing connection to', message.addr)
            sel.unregister(sock)
            sock.close()
        split_data = recv_data.split('
