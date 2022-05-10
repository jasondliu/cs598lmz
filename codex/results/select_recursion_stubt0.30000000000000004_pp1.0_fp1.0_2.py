import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())
    select.select(a, [], [])

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return 0

    a.append(F())
    select.select(a, [], [], 1)

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            return 0

    a.append(F())
    select.select(a, [], [], 1, 1)

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            test_select_mutated4()
            return 0

    a.append(F())
    select.select(a, [], [], 1, 1, 1)

def test_select_mutated5():
    a = []

    class F:
        def fileno(self):

