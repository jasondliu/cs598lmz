import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [F()], [F()], 0)

def test_select_keyboardinterrupt():
    a = []

    class F:
        def fileno(self):
            raise KeyboardInterrupt
            return a.pop()

    select.select([F()], [F()], [F()], 0)

def test_select_keyboardinterrupt2():
    a = []

    class F:
        def fileno(self):
            raise KeyboardInterrupt
            return a.pop()

    try:
        select.select([F()], [F()], [F()], 0)
    except KeyboardInterrupt:
        pass
    else:
        assert False, "Did not raise"

def test_select_keyboardinterrupt3():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    try:
        select.select([F()], [F()], [F()], 0)
    except KeyboardInterrupt:
        pass
