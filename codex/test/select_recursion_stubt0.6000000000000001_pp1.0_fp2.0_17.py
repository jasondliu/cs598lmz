import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    select.select([F()], a, a, 0)

def test_select_large_fd():
    a = []
    b = []

    for i in range(1024):
        a.append(i)
        b.append(i+1)

    select.select(a, b, b, 0)

def test_select_bad_list():
    # Verify that select() only accepts lists
    try:
        select.select(1, 2, 3, 4)
    except TypeError:
        pass
    else:
        raise AssertionError("select didn't raise TypeError")

def test_select_large_timeout():
    # Issue #12043: Python 2.x select.select() uses a double to represent
    # the timeout, so the maximum timeout is platform-dependent.
    # On Windows, the maximum timeout is about 26.8 days.
    # On Linux, the maximum timeout is about 248 days.
    # On OS X, the maximum timeout is about 8.2 minutes.
    max_int = sys.maxsize
