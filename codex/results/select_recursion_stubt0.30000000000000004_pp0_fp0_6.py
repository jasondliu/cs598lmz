import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [F()], [F()], 0)

def test_select_keyboardinterrupt():
    class F:
        def fileno(self):
            raise KeyboardInterrupt
    try:
        select.select([F()], [F()], [F()], 0)
    except KeyboardInterrupt:
        pass

def test_select_error():
    class F:
        def fileno(self):
            raise OSError
    try:
        select.select([F()], [F()], [F()], 0)
    except OSError:
        pass

def test_select_closed():
    class F:
        def fileno(self):
            return -1
    try:
        select.select([F()], [F()], [F()], 0)
    except OSError:
        pass

def test_select_closed_error():
    class F:
        def fileno(self):
            raise OSError
        def close(self):
            raise
