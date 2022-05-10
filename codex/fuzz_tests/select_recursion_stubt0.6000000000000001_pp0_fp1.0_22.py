import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [F()], [F()])

def test_select_errors():
    class F:
        def fileno(self):
            raise OSError("abc")

    select.select([F()], [F()], [F()])

def test_select_keyboardinterrupt():
    class F:
        def fileno(self):
            raise KeyboardInterrupt

    select.select([F()], [F()], [F()])
