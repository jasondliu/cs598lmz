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

    select.select([F()], [], [], 0)

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            return a.pop()

    select.select([], [F()], [])

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            test_select_mutated4()
            return a.pop()

    select.select([], [F()], [], 0)

def test_select_mutated5():
    a = []

    class F:
        def fileno(self):
            test_select_mutated5()
            return a.pop()

