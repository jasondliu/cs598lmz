import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    def f():
        a.append(F())
        return a[-1]

    fd = f()
    assert select.select([fd], [fd], [fd], 0) == ([fd], [fd], [fd])

def test_select_error():
    import select
    import errno
    import os
    import sys

    # XXX: we need a better way to find an invalid fd
    invalid_fd = -1
    while True:
        try:
            os.fstat(invalid_fd)
        except OSError as e:
            if e.errno == errno.EBADF:
                break
            raise
        invalid_fd -= 1
    else:
        raise ValueError("couldn't find an invalid fd")

