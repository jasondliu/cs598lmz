import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    def f():
        select.select([F()], [], [])

    a = [0, 1]
    raises(ValueError, f)

    a = [0, 0]
    raises(ValueError, f)

    a = [0]
    f()

    a = []
    raises(ValueError, f)

    a = [0]
    raises(ValueError, f)

def test_select_error():
    a = []

    class F:
        def fileno(self):
            a.pop()
            raise ValueError

    def f():
        select.select([F()], [], [])

    a = [0]
    raises(ValueError, f)

    a = [0, 0]
    raises(ValueError, f)

    a = [0, 1]
    raises(ValueError, f)

    a = []
    raises(ValueError, f)

    a = [0]
    raises(ValueError, f)

def test_select_closed_pipe():
    # see
