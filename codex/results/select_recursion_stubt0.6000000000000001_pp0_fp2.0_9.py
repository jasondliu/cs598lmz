import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def close(self):
            a.append(1)

    select.select([F()], [], [], 0)
    assert a
    a.pop()

    select.select([], [F()], [], 0)
    assert a
    a.pop()

    select.select([], [], [F()], 0)
    assert a
    a.pop()

    raises(ValueError, select.select, [], [], [], -1)
    raises(ValueError, select.select, [], [], [], 1e100)
    raises(ValueError, select.select, [], [], [], -1e100)

def test_select_large_fd():
    # Issue #16689: select() should not crash on a large fd, but rather
    # raise an error.
    try:
        import resource
    except ImportError:
        skip("resource module not available")
    try:
        maxfd = resource.getrlimit(resource.RLIMIT_NOFILE)[0]
        if maxfd < 0:
           
