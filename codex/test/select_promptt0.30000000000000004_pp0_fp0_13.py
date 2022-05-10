import select
# Test select.select()

def test_select():
    import select
    import socket

    # Create two sockets.
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind them to the same port.
    s1.bind(('127.0.0.1', 0))
    s2.bind(('127.0.0.1', s1.getsockname()[1]))

    # Make them listen.
    s1.listen(1)
    s2.listen(1)

    # Connect to s1 with s2.
    s2.connect(s1.getsockname())

    # Wait for s1 to be ready to read.
    r, w, x = select.select([s1], [], [])
    if s1 not in r:
        raise TestFailed("s1 not ready to read")

    # Accept the connection.
    connection, address = s1.accept()
