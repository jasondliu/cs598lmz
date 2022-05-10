import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    a.append(F())
    select.select([], [], [])

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 5

    a.append(F())
    select.select([], [], [])

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            a.pop()
            raise ValueError

    a.append(F())
    select.select([], [], [])

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 5

        def close(self):
            a.append(None)

    a.append(F())
    select.select([], [], [])

def test_select_mutated5():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 5
