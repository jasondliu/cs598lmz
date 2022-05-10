import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            raise IndexError
    f = F()
    select.select([f], [], [])
    assert len(a) == 1

def test_select_keyboardinterrupt():
    import errno
    import os
    from _testcapi import raise_exception
    # Issue #11647: select.select() shouldn't swallow KeyboardInterrupt
    # raised by file object's fileno() method.
    class InterruptingFD:
        def fileno(self):
            raise KeyboardInterrupt
    try:
        select.select([InterruptingFD()], [], [])
    except KeyboardInterrupt:
        pass
    else:
        assert False, "didn't raise"
    # Issue #12573: select.select() shouldn't swallow other exceptions
    # raised by file object's fileno() method.
    class ExceptionalFD:
        def fileno(self):
            raise RuntimeError
    try:
        select.select([ExceptionalFD()], [], [])
    except RuntimeError:
        pass
    else:
        assert
