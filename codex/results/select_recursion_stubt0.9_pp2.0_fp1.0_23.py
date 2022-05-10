import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
    a.append(F())

    select.select(a, a, a)

run_tests(__name__, __file__)
