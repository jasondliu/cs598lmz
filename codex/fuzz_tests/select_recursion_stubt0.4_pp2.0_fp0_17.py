import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 42

    select.select([F()], a, a, 0)

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            return 42

    select.select([F()], a, a, 0)
    test_select_mutated()

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            return 42

    select.select([F()], a, a, 0)
    test_select_mutated2()

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            return 42

    select.select([F()], a, a, 0)
    test_select_mutated3()

def test_select_mutated5():
    a = []

    class F:
        def fileno(self):
            return 42

    select.select([F()], a, a, 0)
    test_select_mutated4()

def test_
