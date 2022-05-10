import select
# Test select.select()

def test_select():
    import select
    r, w, e = select.select([], [], [], 1)
    assert len(r) == 0
    assert len(w) == 0
    assert len(e) == 0

def test_select_timeout():
    import select
    import time
    t = time.time()
    r, w, e = select.select([], [], [], 1)
    assert time.time() - t >= 1

def test_select_error():
    import select
    raises(ValueError, select.select, [], [], [], -1)
