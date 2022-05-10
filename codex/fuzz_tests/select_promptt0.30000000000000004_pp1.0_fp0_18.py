import select
# Test select.select

def test_select():
    r, w, x = select.select([], [], [], 0)
    assert r == []
    assert w == []
    assert x == []

def test_select_timeout():
    import time
    start = time.time()
    r, w, x = select.select([], [], [], 1.0)
    end = time.time()
    assert end - start >= 1.0
    assert r == []
    assert w == []
    assert x == []

def test_select_read():
    import os
    r, w, x = select.select([sys.stdin], [], [], 0)
    assert r == [sys.stdin]
    assert w == []
    assert x == []

def test_select_write():
    import os
    r, w, x = select.select([], [sys.stdout], [], 0)
    assert r == []
    assert w == [sys.stdout]
    assert x == []

def test_select_readwrite():
    import os

