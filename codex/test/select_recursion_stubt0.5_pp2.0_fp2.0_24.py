import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    a.append(F())
    try:
        select.select(a, a, a)
    except RuntimeError:
        pass
    except:
        raise

def test_select_error():
    import errno
    import select
    import sys

    # The select module should not raise an exception if an
    # invalid file descriptor is used.
    if sys.platform == 'win32':
        try:
            select.select([-1], [], [])
        except select.error as err:
            assert err.args[0] == errno.EBADF
        else:
            raise RuntimeError("expected an exception")
    else:
        try:
            select.select([-1], [], [])
        except select.error as err:
            assert err.args[0] == errno.EBADF
        else:
            raise RuntimeError("expected an exception")

def test_select_large_fd_set():
    import select
    import sys

    # Issue #11458: select() should not crash on large file descriptor sets

