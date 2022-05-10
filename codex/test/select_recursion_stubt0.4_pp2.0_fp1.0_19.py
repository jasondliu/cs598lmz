import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())

    try:
        select.select([], [], a, 0)
    except ValueError:
        pass
    else:
        assert False, "select() didn't raise ValueError"

def test_select_large_fd():
    # Issue #18791: select() should not crash with a large file descriptor
    # value (greater than FD_SETSIZE)
    try:
        select.select([1e9], [], [])
    except ValueError:
        pass
    else:
        assert False, "select() didn't raise ValueError"

def test_select_large_list():
    # Issue #18791: select() should not crash with a large list size
    # (greater than FD_SETSIZE)
    try:
        select.select(list(range(1e9)), [], [])
    except ValueError:
        pass
    else:
        assert False, "select() didn't raise ValueError"
