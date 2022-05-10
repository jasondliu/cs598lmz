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

    # Test a successful select
    r, w, x = select.select([s1], [s2], [], 1.0)
    assert r == [s1]
    assert w == [s2]
    assert x == []

    # Test a timeout
    r, w, x = select.select([s1], [s2], [], 1.0)
    assert r == []
    assert w == []
    assert x == []

    # Test an exceptional condition
    s1.close()
    r, w, x = select.select([s1], [s2], [], 1.0)
    assert r == []
    assert w == []
    assert x == [s1]

    # Test a successful poll
    p = select.poll()
    p.register(s2, select.POLLIN)
