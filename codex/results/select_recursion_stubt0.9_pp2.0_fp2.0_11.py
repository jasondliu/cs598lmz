import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    f = F()
    a.append(f)

    with raises(UnsupportedOperation):
        select.select(a, fd_setsize=1)

def test_select_large_set():
    # Small fd_setsize, so the test runs quickly
    fd_setsize = 8
    if hasattr(select, 'PY_FD_SETSIZE'):
        select.PY_FD_SETSIZE = fd_setsize
    else:
        # required on PyPy and CPython 3.8+
        select.set_fd_setsize(fd_setsize)

    # We create 10,000 file descriptors and make sure that the largest one
    # becomes the first one in the fd set (in a portable way). See #12086 and #12132.
    # fd_setsize must be <= 32 on win32
    pipes = [os.pipe() for i in range(10000)]
    r, w, x = select.select([], pipes, [])
    assert w[0][0] == pipes[-1
