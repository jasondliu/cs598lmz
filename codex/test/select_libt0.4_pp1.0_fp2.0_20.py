import selectors
import queue
import time
import sys

def worker(sel, sock, mask):
    data = sock.recv(100)
    if data:
        print('echoing', repr(data), 'to', sock)
        sock.send(data)
    else:
        print('closing', sock)
        sel.unregister(sock)
        sock.close()

def server(port):
    sel = selectors.DefaultSelector()
    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lsock.bind(('', port))
    lsock.listen()
    print('listening on', (host, port))
    lsock.setblocking(False)
    sel.register(lsock, selectors.EVENT_READ, data=None)

    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
