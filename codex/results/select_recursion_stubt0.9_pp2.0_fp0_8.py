import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    r = [F()]
    res = []

    try:
        res = select.select(r, r, r, 1)
    except (ValueError, IndexError):
        pass
    # This should be safe :-P
    res = select.select(r, r, r, 1)
    res = select.select(r, r, r, 1)
    res = select.select(r, r, r, 1)

def test_select_timer():
    import time

    t1 = time.monotonic()
    r, w, e = select.select([], [], [], 0.1)
    t2 = time.monotonic()
    assert t2 - t1 >= 0.1
    assert t2 - t1 < 0.15
    r, w, e = select.select([], [], [], 0.8)
    t3 = time.monotonic()
    assert t3 - t2 >= 0.8
    assert t3 - t2 < 0.85

def test_select_error
