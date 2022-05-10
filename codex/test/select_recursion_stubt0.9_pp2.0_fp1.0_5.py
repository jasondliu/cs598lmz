import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    select.select([F()], [F()], [F()], 0)
    select.select([F()], a, [F()], 0)
    select.select([F()], a, a, 0)

def test_select_plus():
    a = []
    a += [3]
    select.select([a], [a], [a], 0)
