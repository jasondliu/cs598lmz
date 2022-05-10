import select
# Test select.select()

def test_select():
    import select
    import socket
    import time

    # Create two sockets
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind them to something
    s1.bind(('localhost', 0))
    s2.bind(('localhost', 0))

    # Have s1 listen
    s1.listen(1)

    # Connect s2 to s1
    s2.connect(s1.getsockname())

    # s1 accepts the connection
    s3, addr = s1.accept()

    # s2 sends a byte
    s2.send(b'x')

    # We should be able to read the byte with select
    r, w, e = select.select([s3], [], [], 1.0)
    assert r == [s3]
    assert s3.recv(1) == b'x'

    # s3 should be in the write
