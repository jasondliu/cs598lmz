import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    def f():
        a.append(1)
        select.select([F()], [], [], 0)

    f()
    print a
    assert a == [1]

def test_select_error():
    import errno
    class F:
        def fileno(self):
            return 0
    try:
        select.select([F()], [], [], 0)
    except OSError, e:
        assert e.errno == errno.EBADF
    else:
        assert False, "expected OSError"

def test_select_error2():
    import errno
    class F:
        def fileno(self):
            return 0
        def close(self):
            raise OSError(errno.EBADF, "")
    try:
        select.select([F()], [], [], 0)
    except OSError, e:
        assert e.errno == errno.EBADF
    else:
        assert False, "expected OSError"


