import select
# Test select.select

def test_select():
    r, w, x = select.select([], [], [], 0.1)
    assert r == w == x == [], (r, w, x)

def test_select_timeout():
    import time
    t1 = time.time()
    r, w, x = select.select([], [], [], 0.1)
    t2 = time.time()
    assert t2 - t1 < 0.15, (t2 - t1)

def test_select_timeout_zero():
    import time
    t1 = time.time()
    r, w, x = select.select([], [], [], 0)
    t2 = time.time()
    assert t2 - t1 < 0.1, (t2 - t1)

def test_select_read_listen_socket():
    import socket
    s = socket.socket()
    s.bind(('127.0.0.1', 0))
    s.listen(1)
