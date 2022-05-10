import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    try:
        select.select([f], [], [])
    except IndexError:
        pass
    else:
        assert False, "select.select did not raise an exception"

def test_select_keyboardinterrupt():
    a = []

    class F:
        def fileno(self):
            raise KeyboardInterrupt
            return a.pop()

    f = F()
    try:
        select.select([f], [], [])
    except KeyboardInterrupt:
        pass
    else:
        assert False, "select.select did not raise an exception"

def test_select_keyboardinterrupt_2():
    a = []

    class F:
        def fileno(self):
            a.pop()
            raise KeyboardInterrupt

    f = F()
    try:
        select.select([f], [], [])
    except KeyboardInterrupt:
        pass
    else:
        assert False, "select.select did not raise an exception"
