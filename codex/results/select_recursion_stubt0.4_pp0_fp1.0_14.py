import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    select.select([F()], [], [], 0)
    select.select([], [F()], [], 0)
    select.select([], [], [F()], 0)
    select.select([F()], [F()], [F()], 0)
    select.select([a], [a], [a], 0)

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            return 1

    select.select([a], [a], [a], 0)
    select.select([F()], [F()], [F()], 0)

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            return 1

    select.select([a], [a], [a], 0)
    select.select([F()], [F()], [F()], 0)
    select.select([a], [a], [a], 0)

def test_select_mutated4():
    a = []

    class
