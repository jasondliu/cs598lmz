import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    select.select([F()], [], [], 0)
    assert a == [1]

def test_select_fd_error():
    class F:
        def fileno(self):
            raise ValueError

    select.select([F()], [], [], 0)

def test_select_bad_fd():
    import errno
    try:
        select.select([-1], [], [], 0)
    except OSError as e:
        assert e.errno == errno.EBADF
    else:
        assert False, "select(-1, [], [], 0) didn't raise OSError"

def test_select_bad_fd_2():
    import errno
    try:
        select.select([-1, -2], [], [], 0)
    except OSError as e:
        assert e.errno == errno.EBADF
