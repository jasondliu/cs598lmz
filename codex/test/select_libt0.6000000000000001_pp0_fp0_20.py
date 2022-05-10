import selectors
import socket
import types
import hashlib
import time

sel = selectors.DefaultSelector()

#HOST = '127.0.0.1'
#HOST = '10.0.0.30'
HOST = '192.168.1.100'
PORT = 65432

def get_file_md5(file_path):
    m = hashlib.md5()
    with open(file_path,'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            m.update(data)
    return m.hexdigest()

def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print('accepted connection from', addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
