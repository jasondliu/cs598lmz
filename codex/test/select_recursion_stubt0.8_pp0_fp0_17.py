import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    def f(x):
        a.append(0)
        return x

    select.select([f(F())], [f(F())], [f(F())], 0.02)
    test_select_mutated()
    # if the above does not segfault, then we're happy.

def test_select_large_timeout():
    # we're testing if a large timeout is set to non-infinite
    # internally, which caused it to segfault on some platforms
    # due to an integer overflow (see http://bugs.python.org/issue9937)
    assert select.select([], [], [], sys.maxsize) == ([], [], [])

def test_select_fdset_size():
    # Issue #30236: Make sure that the size of the fdset is not
    # greater than FD_SETSIZE
    assert test_support.FD_SETSIZE > 10
    large_fd = os.open(test_support.TESTFN, os.O_RDONLY)
