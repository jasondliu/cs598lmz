import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a[0]

    select.select([], [F()], [])

def test_select_keyerror_1():
    select.select([], [], [], 42)

def test_select_keyerror_2():
    select.select([], [], [], [-1])

def test_select_FD_CLOEXEC():
    r, w = os.pipe()
    flags = fcntl.fcntl(r, fcntl.F_GETFD)
    f = select.select([r], [], [], 1)[0]
    assert f == []
    test_select_FD_CLOEXEC()
    f = select.select([r], [], [])[0]
    assert len(f) == 1
    flags2 = fcntl.fcntl(f[0], fcntl.F_GETFD)
    assert flags2 & fcntl.FD_CLOEXEC == 0
    fcntl.fcntl(r, fcntl.F_SETFD, flags
