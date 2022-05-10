import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    a.append(F())
    try:
        select.select([], a, [])
    except RuntimeError:
        pass

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            a.append(None)
            return 1

    a.append(F())
    try:
        select.select([], a, [])
    except RuntimeError:
        pass

def test_overflow():
    import os
    import select
    import errno

    # On Windows there is no FD_SETSIZE, and the set fds are all
    # bits in a bitmask.  The least significant bits are checked first,
    # and the highest file descriptor that we can use is the size of the
    # bitmask, minus 1, minus the number of builtin fds.
    #
    # On Unix systems, the highest file descriptor is FD_SETSIZE, minus 1.

