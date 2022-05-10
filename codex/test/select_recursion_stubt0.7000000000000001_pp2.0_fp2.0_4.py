import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    a.append(F())
    select.select([F()], [F()], [F()], 0)
    a.append(F())

test_select_mutated()
