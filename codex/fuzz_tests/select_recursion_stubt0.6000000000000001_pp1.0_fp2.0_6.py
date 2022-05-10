import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    select.select([F()], [], [])
    assert a == [1]

def test_select_closed():
    class F:
        def fileno(self):
            return 3

    f = F()
    os.close(3)
    raises(OSError, select.select, [f], [], [])

def test_fd_exception():
    class F:
        def fileno(self):
            raise OSError

    f = F()
    raises(OSError, select.select, [f], [], [])

def test_select_str():
    # sys.stdin is a str() on PyPy, but it's an int() on CPython
    if isinstance(sys.stdin, int):
        class F:
            def fileno(self):
                return 'foo'

        f = F()
        raises(TypeError, select.select, [f], [], [])

def test_select_bad_arg():
    class F:
        def fileno(self):

