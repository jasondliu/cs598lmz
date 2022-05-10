import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    a.append(F())
    try:
        select.select(a, a, a)
    except ValueError:
        pass
    else:
        assert False, "select didn't raise ValueError"

def test_select_large_fd():
    # Issue #14056: select() should not crash with large file descriptors.
    # (This test is only meaningful on 64-bit platforms.)
    if sys.maxsize < 2**32:
        pytest.skip("test only meaningful on 64-bit platforms")
    try:
        select.select([2**31], [], [])
    except ValueError:
        pass
    else:
        assert False, "select didn't raise ValueError"

def test_select_large_list():
    # Issue #14056: select() should not crash with large lists.
    try:
        select.select([], [], [], 0, [0] * (sys.maxsize // 4))
    except OverflowError:
        pass
