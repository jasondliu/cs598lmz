import select
# Test select.select with timeout and three sockets.
import socket
import time

def test(timeout):
    sockets = [socket.socket(), socket.socket(), socket.socket()]
    sockets[0].setblocking(True)
    sockets[1].setblocking(False)
    sockets[2].setblocking(False)
    sockets[0].bind(("127.0.0.1", 0))
    sockets[1].bind(("127.0.0.1", 0))
    sockets[2].bind(("127.0.0.1", 0))
    sockets[0].listen(1)
    sockets[1].listen(1)
    sockets[2].listen(1)
    for sock in sockets:
        print(sock.getsockname())
    (r, w, e) = select.select(sockets, [], [], timeout)
    for sock in r:
        print(sock.getsockname())
    for sock in e:
        print(sock.getsockname())
    for sock in sockets:
        sock.close()

