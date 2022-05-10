import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 10
        def close(self):
            pass

    class F2:
        def fileno(self):
            return 11
        def close(self):
            pass

    f = F()
    f2 = F2()
    r, w, x = select.select([f, f2], [], [])
    assert a == [1]
    assert r == [f2]

def test_select_closed_fd():
    import os
    import select
    import sys

    # Issue #23458: select(closed_fd, [], [])
    # should not crash.
    if sys.platform == 'win32':
        # On Windows, select() always raises an exception when
        # closed_fd is passed.
        closed_fd = os.open(os.devnull, os.O_RDONLY)
        os.close(closed_fd)
        with pytest.raises(OSError):
            select.select([closed_fd], [], [])
    else:
        # On Unix, select() should
