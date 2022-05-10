import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 1

    select.select([F()], [], [])
    assert a == [1]

def test_select_keyboard_interrupt():
    py.test.raises(KeyboardInterrupt, select.select, [], [], [])

    class F:
        def fileno(self):
            raise KeyboardInterrupt

    py.test.raises(KeyboardInterrupt, select.select, [F()], [], [])

def test_select_error():
    class F:
        def fileno(self):
            raise OSError(errno.EBADF, "")

    py.test.raises(OSError, select.select, [F()], [], [])

def test_select_large_fd():
    import sys
    if not hasattr(sys, 'getcheckinterval'):
        skip("Only on CPython")
    sys.setcheckinterval(1)
