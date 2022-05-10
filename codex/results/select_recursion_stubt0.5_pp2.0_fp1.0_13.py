import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def read(self):
            a.append(1)
            return b'x'

    f = F()
    select.select([f], [], [])
    assert a == [1]
    assert select.select([f], [], []) == ([f], [], [])
    assert a == [1, 1]

def test_select_error_on_close():
    class F:
        def fileno(self):
            return 0

        def close(self):
            raise OSError(errno.EBADF, "Bad file descriptor")

    f = F()
    select.select([f], [], [])

def test_select_error_on_fileno():
    class F:
        def fileno(self):
            raise OSError(errno.EBADF, "Bad file descriptor")

    f = F()
    select.select([f], [], [])

def test_select_error_on_read():
    class F:
        def fileno(self):
            return 0

       
