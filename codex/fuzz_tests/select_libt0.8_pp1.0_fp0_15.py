import selectors
import socket
import types
import os

sel = selectors.DefaultSelector()
n_conns = 0

def accept(sock, mask):
    global n_conns
    conn, addr = sock.accept()  # Should be ready
    conn.setblocking(False)
    n_conns += 1
    print('accepted', conn, 'from', addr, n_conns, 'connections')
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    global n_conns
    data = conn.recv(1024)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn, 'from', n_conns, 'connections')
        conn.send(data)
        sel.modify(conn, selectors.EVENT_WRITE, read)
    else:
        print('closing', conn, 'from', n_conns, 'connections')
        sel.unregister(conn)
        conn.close()

