import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            raise Exception('never reached')

    select.select([F()], a, a, 0.01)

def test_select_errno():
    a = []
    import errno
    class F:
        def fileno(self):
            raise OSError(errno.EINTR, "I am interrupted")
            raise Exception('never reached')

    select.select([F()], a, a, 0.01)
