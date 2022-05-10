import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop(0)

    select.select([F()], [F()], [F()], 0)
