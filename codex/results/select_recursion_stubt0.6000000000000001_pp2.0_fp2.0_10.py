import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [], [])

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return a.pop()

    select.select([], [F()], [])

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            return a.pop()

    select.select([], [], [F()])


def test_select_exception():
    class F:
        def fileno(self):
            raise IOError

    select.select([F()], [], [])
    select.select([], [F()], [])
    select.select([], [], [F()])

def test_select_exception2():
    class F:
        def fileno(self):
            raise AttributeError

    select.select([F()], [], [])
    select.select([],
