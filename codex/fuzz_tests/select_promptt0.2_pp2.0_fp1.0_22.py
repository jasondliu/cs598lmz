import select
# Test select.select()

def test_select():
    import select
    import socket
    import time

    # Set up two sockets
    s1, s2 = socket.socketpair()
    s1.setblocking(0)
    s2.setblocking(0)

    # Test that they are readable and writable
    for i in range(5):
        r, w, e = select.select([s1], [s2], [], 0.1)
        assert r == [s1]
        assert w == [s2]
        assert e == []
        r, w, e = select.select([s2], [s1], [], 0.1)
        assert r == [s2]
        assert w == [s1]
        assert e == []

    # Test that they are not readable or writable
    for i in range(5):
        r, w, e = select.select([s1], [s2], [], 0.1)
        assert r == []
        assert w == []
        assert e == []
        r, w, e = select.select([s
