import select
# Test select.select

import select
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 0))
s.listen(1)

def test_select():
    r, w, x = select.select([s], [], [], 0.1)
    assert len(r) == 1
    assert r[0] == s
    assert len(w) == 0
    assert len(x) == 0

test_select()

def test_select_timeout():
    import time
    t1 = time.time()
    r, w, x = select.select([s], [], [], 0.1)
    t2 = time.time()
    assert 0.1 <= t2 - t1 <= 0.2

test_select_timeout()

def test_select_timeout_zero():
    import time
    t1 = time.time()
    r, w, x = select.select([s], [], [], 0)
    t2 = time.time()
    assert 0 <= t
