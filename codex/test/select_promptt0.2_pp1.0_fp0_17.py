import select
# Test select.select()

def test_select():
    import select
    import socket
    import time
    # Create two sockets
    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lsock.bind(('localhost', 0))
    lsock.listen(1)
    port = lsock.getsockname()[1]
    csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    csock.connect(('localhost', port))
    ssock, addr = lsock.accept()
    # Test basic operation
    assert select.select([csock], [], [], 0.0) == ([csock], [], [])
    assert select.select([csock], [], [], 0.0) == ([], [], [])
    # Test exceptional condition
    csock.send(b"x")
    assert select.select([ssock], [], [], 0.0) == ([ssock], [], [])
