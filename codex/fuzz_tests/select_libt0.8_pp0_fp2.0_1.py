import selectors
import socket

import web_server

sel = selectors.DefaultSelector()

def accept(sock, mask):
    print("accept")
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)


def read(conn, mask):
    print("read")
    web_server.read(conn)
    sel.unregister(conn)

if __name__ == "__main__":
    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lsock.bind((web_server.HOST, web_server.PORT))
    lsock.listen()
    print('listening on', (web_server.HOST, web_server.PORT))
    lsock.setblocking(False)
    sel.register(lsock, selectors.EVENT_READ, accept)

    while True:
        events = se
