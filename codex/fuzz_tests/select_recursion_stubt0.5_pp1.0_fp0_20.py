import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    def f():
        a.append(0)
        select.select([F()], [], [])

    raises(RuntimeError, f)
    assert len(a) == 1

def test_select_keyboardinterrupt():
    # Issue #14091.
    import _socket
    a = []

    class F:
        def fileno(self):
            # Raise an exception in the middle of select()
            a.append(0)
            raise KeyboardInterrupt
        def close(self):
            a.append(1)

    def f():
        a.append(2)
        select.select([F()], [], [])

    raises(KeyboardInterrupt, f)
    assert a == [2, 0, 1]

def test_select_keyboardinterrupt_2():
    # Issue #14091.
    import _socket
    a = []

    class F:
        def fileno(self):
            # Raise an exception in the middle of select()
            a.append(0)
            raise KeyboardInterrupt

