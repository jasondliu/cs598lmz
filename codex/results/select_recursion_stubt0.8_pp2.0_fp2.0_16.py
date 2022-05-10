import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 42

    r, w, e = select.select([F()], a, a)
    r, w, e = select.select(a, [F()], a)
    r, w, e = select.select(a, a, [F()])
    r, w, e = select.select([], [], [])


def test_select_large_fd():
    # If a select() call doesn't support the given fd, it returns either
    # -1 or raises an exception.
    #
    # However, some select() implementations support large fds, but not really
    # large ones. On AIX, for example, FD_SETSIZE (the maximum value of an
    # fd that can be passed to select) is 1024.  So we must not pass a
    # fd larger than FD_SETSIZE to select().
    #
    # This test exercises this condition by passing a large fd to select(),
    # which, depending on the platform and configuration, may or may not
    # be less than FD_SETSIZE.
    #
    # Note that this
