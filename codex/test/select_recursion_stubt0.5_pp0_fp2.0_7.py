import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [], [], 0.0)

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return a.pop()

    select.select([], [F()], [], 0.0)

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            return a.pop()

    select.select([], [], [F()], 0.0)

def test_select_mutated_error():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_error()
            return a.pop()

    try:
        select.select([F()], [F()], [F()], 0.0)
    except ValueError:
        pass

