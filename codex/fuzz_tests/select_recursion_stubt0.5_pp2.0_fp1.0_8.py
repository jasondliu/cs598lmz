import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
        def read(self):
            a.append(self)
            return ""
        def close(self):
            pass

    select.select([F()], [], [])

def test_select_keyboardinterrupt():
    a = []

    class F:
        def fileno(self):
            test_select_keyboardinterrupt()
            return len(a)
        def read(self):
            a.append(self)
            raise KeyboardInterrupt
        def close(self):
            pass

    select.select([F()], [], [])

def test_select_error():
    a = []

    class F:
        def fileno(self):
            test_select_error()
            return len(a)
        def read(self):
            a.append(self)
            raise OSError
        def close(self):
            pass

    select.select([F()], [], [])

def test_select_closed():
    a = []

    class F:
        def fileno(self):
