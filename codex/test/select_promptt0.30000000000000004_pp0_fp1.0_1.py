import select
# Test select.select()

def test_select():
    import select
    r, w, e = select.select([], [], [], 0.1)
    assert r == w == e == [], "select([], [], [], 0.1) should return 3 empty lists"

def test_select_timeout():
    import select
    import time
    start = time.time()
    r, w, e = select.select([], [], [], 0.1)
    stop = time.time()
    assert stop - start >= 0.1, "select([], [], [], 0.1) should block for at least 0.1 seconds"

def test_select_read():
    import select
    import socket
    s = socket.socket()
    s.bind(('', 0))
    s.listen(1)
    r, w, e = select.select([s], [], [], 0.1)
    assert r == [s], "select([s], [], [], 0.1) should return [s] in the first list"

