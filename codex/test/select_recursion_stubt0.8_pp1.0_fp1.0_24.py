import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.pop()
            return 42

    select.select([F()], [F()], [], 0)
    select.select([], [F()], [], 0)
    select.select([], [], [F()], 0)
    select.select([F()], [], [F()], 0)
