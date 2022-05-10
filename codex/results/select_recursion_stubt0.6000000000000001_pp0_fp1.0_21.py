import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    select.select([], [F()], [], 0.0)

def test_select_interrupted():
    a = []

    class F:
        def fileno(self):
            return len(a)

    select.select([F()], [], [], 0.0)

def test_select_interrupted2():
    a = []

    class F:
        def fileno(self):
            return len(a)

    select.select([F()], [F()], [], 0.0)

def test_select_interrupted3():
    a = []

    class F:
        def fileno(self):
            return len(a)

    select.select([F()], [], [F()], 0.0)

def test_select_interrupted4():
    a = []

    class F:
        def fileno(self):
            return len(a)

    select.select([F()], [F()], [F()], 0.0)

def test_select_interrupted5():
    a = []


