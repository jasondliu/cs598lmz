import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], a, a, 0)

def test_select_error():
    a = []
    select.select(a, a, a, 0)

def test_select_keyboardinterrupt():
    a = []
    select.select(a, a, a, 0)
    raise KeyboardInterrupt

def test_select_exception():
    a = []
    select.select(a, a, a, 0)
    raise Exception

def test_select_mutated_keyboardinterrupt():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_keyboardinterrupt()
            return 0

    select.select([F()], a, a, 0)
    raise KeyboardInterrupt

def test_select_mutated_exception():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_exception()
            return 0

    select.select([F()], a, a, 0)
    raise Exception
