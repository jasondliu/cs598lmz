import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    class G:
        def fileno(self):
            a.append(1)
            return 1

    select.select([F()], [], [])
    select.select([G()], [], [])
    assert a == [1]

def test_select_error():
    import errno
    class F:
        def fileno(self):
            return 0
        def close(self):
            pass
    try:
        select.select([F()], [], [])
    except OSError as e:
        assert e.errno == errno.EBADF
    else:
        assert False, "Expected OSError"

def test_select_error_2():
    import errno
    class F:
        def fileno(self):
            return 0
        def close(self):
            pass
    try:
        select.select([F()], [F()], [])
    except OSError as e:
        assert e.errno == errno.EBADF
