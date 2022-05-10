import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
    a.append(F())

    a.append(sys.stdin)
    r,w,e = select.select(a, a, a, 0)
    assert len(r) == 1
    assert len(w) == 1
    assert len(e) == 1

def test_reselect():
    a = []
    a.append(sys.stdin)
    r,w,e = select.select(a, a, a, 0)
    assert len(r) == 1
    assert len(w) == 1
    assert len(e) == 1
    r,w,e = select.select(a, a, a, 0)
    assert len(r) == 1
    assert len(w) == 1
    assert len(e) == 1

def test_select_timeout():
    import time
    t = time.time()
    r,w,e = select.select([], [], [], 0.5)
    t = time.time() - t
    assert t >= 0.5

def test_select_timeout_neg():
