import selectors
import socket
import time

def main():
    selector = selectors.DefaultSelector()

    host = '127.0.0.1'
    port = 8091
    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lsock.bind((host, port))
    lsock.listen()
    print('listening on ', (host, port))
    lsock.setblocking(False)
    selector.register(lsock, selectors.EVENT_READ, data=None)

    while running:
        events = selector.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)
    print('shutting down')
    selector.close()

def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print('accepted connection from', addr)
    conn.setblocking(False)
