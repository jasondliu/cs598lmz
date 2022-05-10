import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [], [], 10)

def test_FD_CLOEXEC():
    import fcntl
    for fd in (0, 1, 2):
        old = fcntl.fcntl(fd, fcntl.F_GETFD)
        fcntl.fcntl(fd, fcntl.F_SETFD, old | fcntl.FD_CLOEXEC)

def test_set_inheritable():
    import os
    f = os.open(os.curdir, os.O_RDONLY)
    os.set_inheritable(f, True)
    os.close(f)

class TestFcntl(unittest.TestCase):
    def test_flags(self):
        import fcntl
        fcntl.F_DUPFD

    def test_bad_fileno(self):
        import fcntl
