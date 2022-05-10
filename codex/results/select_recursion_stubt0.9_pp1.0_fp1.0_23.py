import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    a.append(F())
    try:
        select.select([], [], a)
    except ValueError:
        return
    raise Exception("Did not raise ValueError")

import socket

def test_socket_sock_closed():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.close()
    try:
        sock.send("x")
    except socket.error:
        return
    raise Exception("Did not raise socket.error")

def test_socket_setblocking():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(0)
    s.setblocking(1)

def test_socket_timeout():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(0)
    try:
        s.connect(("10.0.0.42", 12345))
    except socket.error:
        return
    raise Exception("Did not raise socket
