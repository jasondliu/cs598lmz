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

    # Wait for the connection
    s1, addr = s1.accept()

    # Now we should be able to select on them
    r, w, e = select.select([s1], [s2], [])
    assert r == [s1]
    assert w == [s2]
    assert e == []

    # Close the sockets
    s1.close()
    s2.close()

def test_select_timeout():
    import select

