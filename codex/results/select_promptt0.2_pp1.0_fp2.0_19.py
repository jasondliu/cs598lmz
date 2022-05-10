import select
# Test select.select()

def test_select():
    import select
    r, w, x = select.select([], [], [], 0.1)
    assert r == []
    assert w == []
    assert x == []

def test_select_timeout():
    import select
    import time
    t1 = time.time()
    r, w, x = select.select([], [], [], 0.1)
    t2 = time.time()
    assert r == []
    assert w == []
    assert x == []
    assert t2 - t1 >= 0.1

def test_select_timeout_0():
    import select
    import time
    t1 = time.time()
    r, w, x = select.select([], [], [], 0.0)
    t2 = time.time()
    assert r == []
    assert w == []
    assert x == []
    assert t2 - t1 < 0.1

def test_select_timeout_neg():
    import select
    import time
    t1 = time.time()
   
