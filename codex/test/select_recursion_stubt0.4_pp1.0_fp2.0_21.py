import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [F()], [F()], 1)

def test_select_keyboardinterrupt():
    class F:
        def fileno(self):
            raise KeyboardInterrupt

    try:
        select.select([F()], [F()], [F()], 1)
    except KeyboardInterrupt:
        pass
    else:
        raise AssertionError("expected KeyboardInterrupt")

def test_select_interrupted():
    class F:
        def fileno(self):
            raise InterruptedError

    try:
        select.select([F()], [F()], [F()], 1)
    except InterruptedError:
        pass
    else:
        raise AssertionError("expected InterruptedError")

def test_select_interrupted_timeout():
    class F:
        def fileno(self):
            raise InterruptedError

    select.select([F()], [F()], [F()], 1)

