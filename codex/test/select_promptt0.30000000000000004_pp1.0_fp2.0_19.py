import select
# Test select.select()

def test_select():
    import select
    r, w, x = select.select([], [], [], 1.0)
    assert len(r) == 0
    assert len(w) == 0
    assert len(x) == 0

def test_select_timeout():
    import select
    import time
    start = time.time()
    r, w, x = select.select([], [], [], 1.0)
    assert len(r) == 0
    assert len(w) == 0
    assert len(x) == 0
    assert time.time() - start < 2.0

def test_select_read():
    import select
    import socket
    s = socket.socket()
    s.bind(('localhost', 0))
    s.listen(1)
    r, w, x = select.select([s], [], [], 1.0)
    assert len(r) == 1
    assert r[0] is s
    assert len(w) == 0
    assert len(x) == 0

