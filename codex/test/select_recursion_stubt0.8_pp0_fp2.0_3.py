import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    f = F()
    select.select([a], [a], [a], 0.0)
    a.append(f)
    select.select([a], [a], [a], 0.0)
    del a
