import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    def f(x):
        a.append(x)
        return x

    select.select([F()], [], [], 1)
    assert a == []

    select.select([f(1)], [], [], 1)
    assert a == [1]

    select.select([f(1), f(2)], [], [], 1)
    assert a == [1, 1, 2]

def test_select_error():
    import errno
    class F:
        def fileno(self):
            raise OSError(errno.EBADF, "bad file descriptor")
    r,w,x = select.select([F()], [], [])
    assert r == []
    assert w == []
    assert x == []

def test_select_timeout():
    import time
    start = time.time()
    r, w, x = select.select([], [], [], 1)
    assert time.time()-start < 1.5

