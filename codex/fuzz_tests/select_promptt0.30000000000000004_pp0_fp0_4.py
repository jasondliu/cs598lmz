import select
# Test select.select

def test_select():
    import select
    import socket
    import time
    import os

    # Create a pair of connected sockets
    if os.name == "nt":
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', 0))
        sock.listen(1)
        csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        csock.connect(sock.getsockname())
        ssock, addr = sock.accept()
    else:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.bind(b'\0select-test')
        sock.listen(1)
        csock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        csock.connect(b'\0select-test')
        ssock, addr = sock.accept()

    # Set the sockets to non-blocking
    sock.setblocking(False)
   
