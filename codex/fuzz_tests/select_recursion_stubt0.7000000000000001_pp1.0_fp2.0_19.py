import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 42

    a.append(F())
    try:
        select.select([], a, [], 0.0)
    except ValueError:
        pass

def test_select_opened_file():
    f = open(__file__)
    try:
        select.select([f], [], [], 0.0)
    finally:
        f.close()

def test_select_large_fd():
    # Issue #14114: select() should not accept file descriptors that are too
    # large.
    # This test is only relevant on 32 bit systems, as on 64 bit systems this
    # test simply verifies that select() accepts valid file descriptors.
    if hasattr(sys, 'maxint') and sys.maxint < 2**32:
        for fd in -1, 2**32:
            try:
                select.select([fd], [], [], 0.0)
            except ValueError:
                pass
            else:
                self.fail("select.select should not accept file descriptor %d" % fd)

def test_
