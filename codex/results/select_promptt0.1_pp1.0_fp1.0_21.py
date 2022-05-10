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

    # s1 should be ready to accept
    r, w, e = select.select([s1], [], [], 1)
    assert r == [s1]

    # Accept the connection
    conn, addr = s1.accept()

    # s2 should be ready to send
    r, w, e = select.select([], [s2], [], 1)
    assert w == [s2]

    # Send some data
    s2.send(
