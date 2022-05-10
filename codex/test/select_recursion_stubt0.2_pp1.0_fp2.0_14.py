import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    def f():
        a.append(1)
        return 1

    select.select([F()], [], [], 0)
    select.select([f()], [], [], 0)
    assert a == [1]

def test_select_keyboard_interrupt():
    # Issue #12091: select() should not swallow KeyboardInterrupt
    class F:
        def fileno(self):
            raise KeyboardInterrupt
    try:
        select.select([F()], [], [], 0)
    except KeyboardInterrupt:
        pass
    else:
        assert False, "select() should raise KeyboardInterrupt"

def test_select_error():
    # Issue #12091: select() should not swallow errors
    class F:
        def fileno(self):
            raise OSError
    try:
        select.select([F()], [], [], 0)
    except OSError:
        pass
    else:
        assert False, "select() should raise OSError"

