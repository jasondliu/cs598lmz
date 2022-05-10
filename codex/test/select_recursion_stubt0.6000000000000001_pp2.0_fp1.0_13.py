import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 1
        def close(self):
            pass
    f = F()

    r,w,e = select.select([f],[],[],0)
    assert a == [1]
    assert r == [f]
    assert w == []
    assert e == []


def test_select_large_fds():
    # Issue #17091: select() should accept large file descriptors.
    # The exact value of FD_SETSIZE is platform-dependent, but on Linux
    # it is typically 1024.
    import fcntl

    with open('/dev/null', 'rb') as fd:
        for fdnum in range(FD_SETSIZE - 1, FD_SETSIZE + 2):
            try:
                fcntl.fcntl(fd, fcntl.F_DUPFD, fdnum)
            except OSError:
                pass
            else:
                try:
                    fd_set = select.select([fd], [], [], 0)
                finally:
                    os
