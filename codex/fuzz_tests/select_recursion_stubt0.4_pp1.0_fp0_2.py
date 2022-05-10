import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [F()], [F()], 1)

def test_select_keyboardinterrupt():
    a = []

    class F:
        def fileno(self):
            raise KeyboardInterrupt
            return a.pop()

    try:
        select.select([F()], [F()], [F()], 1)
    except KeyboardInterrupt:
        pass
    else:
        assert False

def test_select_keyboardinterrupt_2():
    a = []

    class F:
        def fileno(self):
            raise KeyboardInterrupt
            return a.pop()

    try:
        select.select([F()], [F()], [F()], 1)
    except KeyboardInterrupt:
        pass
    else:
        assert False

def test_select_keyboardinterrupt_3():
    a = []

    class F:
        def fileno(self):
            raise KeyboardInterrupt
            return a.pop()

    try:
        select.select([F()], [
