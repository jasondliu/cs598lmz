import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], a, a, 0)
    assert a == []
    select.select(a, [F()], a, 0)
    assert a == []
    select.select(a, a, [F()], 0)
    assert a == []

def test_select_timeout():
    import time
    a = []
    t0 = time.time()
    select.select(a, a, a, 1.0)
    t1 = time.time()
    assert 0.9 <= t1-t0 <= 1.1

def test_select_error():
    import errno
    class F:
        def fileno(self):
            return -1
    try:
        select.select([F()], [], [], 0)
    except OSError as e:
        assert e.errno == errno.EBADF
    else:
        assert False, "expected OSError"

def test_select_bad_timeout():
    import errno
