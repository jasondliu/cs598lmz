import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    def f():
        pass

    def g():
        pass

    def h():
        pass

    vi = [F(), f, g, h]

    select.select(vi, vi, vi, 2)
    assert len(a) == 1

def test_select_interrupted():
    import errno
    class F:
        def fileno(self):
            raise IOError(errno.EINTR, "interrupted")

    def f():
        pass

    def g():
        pass

    def h():
        pass

    vi = [F(), f, g, h]

    # If a system call fails with EINTR, select() should retry the system call.
    select.select(vi, vi, vi, 2)

def test_select_interrupted_on_fileno():
    import errno
    class F:
        def __init__(self):
            self.a = 0

        def fileno(self):
            self.a += 1
