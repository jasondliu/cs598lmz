import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())
    select.select(a, a, a)

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return 0

    a.append(F())
    select.select(a, a, a, 0)
