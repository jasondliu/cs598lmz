import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return sys.__stdin__.fileno()

    a.append(F())
    try:
        r, w, x = select.select([sys.__stdin__], a, a, 0)
        assert r == []
        assert w == [a[0]]
        assert x == []
    finally:
        a.pop()

def test_select_exc():
    import _socket
    exc = OSError(EBADF, "Bad file descriptor")
    class F:
        def fileno(self):
            raise exc
    a = [F()]
    try:
        r, w, x = select.select(a, a, a, 0)
        assert r == []
        assert w == []
        assert x == []
    finally:
        a.pop()

def test_select_bad_fd():
    import _socket
    exc = OSError(EBADF, "Bad file descriptor")
    class F:
        def fileno(self):
            return -1
    a = [F()]
    try:
