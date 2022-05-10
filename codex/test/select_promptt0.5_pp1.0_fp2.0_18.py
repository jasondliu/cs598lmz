import select
# Test select.select()

import socket

def test_select():
    # Create two sockets
    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lsock.bind(('localhost', 50007))
    lsock.listen(1)
    ssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssock.connect(('localhost', 50007))

    # Wait until the sockets are readable/writable
    r, w, e = select.select([lsock, ssock], [], [])
    assert r == [lsock]
    r, w, e = select.select([lsock, ssock], [], [])
    assert r == [ssock]

    # Connect the server and client
    csock, addr = lsock.accept()

    # Wait until the sockets are readable/writable
    r, w, e = select.select([lsock, ssock, csock], [], [])
    assert r == [csock, ssock]

    # Send a message from client to server
