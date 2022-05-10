import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()
    f = F()
    r = select.select([f], [f], [f], 0)
    assert r == ([f], [f], [f])
    py.test.raises(IndexError, "select.select([f], [f], [f], 0)")

def test_select_error():
    import errno
    class F:
        def fileno(self):
            return -1
    f = F()
    py.test.raises(OSError, "select.select([f], [f], [f], 0)")

def test_select_fd():
    import os
    r, w = os.pipe()
    try:
        fd = os.dup(r)
        try:
            r2, w2, x2 = select.select([fd], [], [], 0)
            assert r2 == [fd]
        finally:
            os.close(fd)
    finally:
        os.close(r)
        os.close(w)

def test_select_poll():
