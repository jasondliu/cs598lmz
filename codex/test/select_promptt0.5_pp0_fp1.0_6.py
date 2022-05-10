import select
# Test select.select

def test_select():
    import select
    import socket
    import Queue

    r, w, e = select.select([], [], [], 1)
    assert r == w == e == []

    r, w, e = select.select([], [], [], 0)
    assert r == w == e == []

    s = socket.socket()
    s.setblocking(0)
    try:
        s.bind(('127.0.0.1', 0))
    except socket.error as e:
        # XXX: On some platforms, such as OS X, attempting to bind to
        # a port that is already bound will fail with EINVAL, instead
        # of EADDRINUSE.
        if e.errno not in (errno.EINVAL, errno.EADDRINUSE):
            raise

    r, w, e = select.select([], [], [], 0)
    assert r == w == e == []

    r, w, e = select.select([], [], [], 0)
    assert r == w == e
