import select
# Test select.select

import socket

def test_select():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0))
    s.listen(1)
    s.setblocking(0)
    r, w, x = select.select([s], [s], [s], 0.5)
    assert r == [s]
    assert w == [s]
    assert x == [s]
    r, w, x = select.select([s], [s], [s], 0.5)
    assert r == []
    assert w == []
    assert x == []
    s.close()

def test_select_timeout():
    import time
    start = time.time()
    r, w, x = select.select([], [], [], 0.5)
    assert time.time() - start >= 0.5
    assert r == []
    assert w == []
    assert x == []

