import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [], [])

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 1

    select.select([F()], [], [])

def test_select_closed_2():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 1

    select.select([F()], [F()], [F()])

def test_select_closed_3():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 1

    select.select([F()], [F()], [F()])

def test_select_closed_4():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 1

    select.select([F()], [F()], [F()])

def test_select_closed_5():
    a = []


