import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 42

    for i in range(1000):
        a.append(F())
    try:
        select.select(a, a, a)
    except TypeError:
        pass
