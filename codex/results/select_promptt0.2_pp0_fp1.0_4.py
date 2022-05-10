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

    # s1 should be ready to accept the connection
    r, w, x = select.select([s1], [], [], 0.1)
    assert r == [s1]

    # Accept the connection
    s3, addr = s1.accept()

    # s3 should be ready to send data
    r, w, x = select.select([], [s3], [], 0.1)
    assert w == [s3]

    # Send some
