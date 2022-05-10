import selectors
import sys
import time

from client.client import Client
from client.command_parser import CommandParser
from client.message_parser import MessageParser
from client.message_handler import MessageHandler
from client.terminal_handler import TerminalHandler

sel = selectors.DefaultSelector()

def start_connection(host, port, username):
    client = Client(host, port, username)
    client.connect()
    return client

def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print("accepted connection from", addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)

def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data
