import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()
    f = [F()]
    try:
        select.select([], f, [])
    except RuntimeError:
        pass

def test_select_bad_fd():
    fd = 2**15
    # An fd higher than the FD_SETSIZE is not an error on Windows.
    # Don't check for the OverflowError we expect on all other platforms,
    # because it's not even reported as an error on all versions of
    # Windows, and some platforms do report it (e.g., AIX).
    if sys.platform != 'win32': 
        try:
            fd = 2**15
            select.select([fd], [], [])
        except OverflowError:
            pass

def test_select_fd_cloexec(testcase):
    r, w = os.pipe()
    if hasattr(os, 'set_inheritable'):
        os.set_inheritable(r, False)
    flags = fcntl.fcntl(r, fcntl.F_
