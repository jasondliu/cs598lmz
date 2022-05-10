import selectors
import sys
import types
import os
import logging

log = logging.getLogger('TTT')

sel = selectors.DefaultSelector()

def accept_wrapper(sock):
    log.debug("DEBUG: In accept_wrapper")
    conn, addr = sock.accept()  # Should be ready to read
    log.debug("DEBUG: accepted connection from: %s", str(addr))
    conn.setblocking(False)
    message = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=message)

def service_connection(key, mask):
    log.debug("DEBUG: In service_connection")
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        log.debug("DEBUG: received %r", recv_data
