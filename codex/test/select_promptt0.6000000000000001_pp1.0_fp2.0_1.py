import select
# Test select.select

def test_select():
    r, w, x = select.select([], [], [], 1)
    assert r == []
    assert w == []
    assert x == []
    try:
        r, w, x = select.select([], [], [], -1)
        assert 0 # should raise ValueError
    except ValueError:
        pass

    import socket
    sock = socket.socket()
    sock.bind(('localhost', 0))
    sock.listen(1)
    r, w, x = select.select([sock], [], [], 1)
    assert r == [sock]
    assert w == []
    assert x == []
    sock.close()

# Test select.poll

def test_poll():
    poll = select.poll()
    try:
        poll.register(1)
        assert 0 # should raise ValueError
    except ValueError:
        pass

    import socket
    sock = socket.socket()
    sock.bind(('localhost', 0))
    sock.listen(1)
    poll.register
