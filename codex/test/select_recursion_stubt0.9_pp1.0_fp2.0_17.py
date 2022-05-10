import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(12)

    r = select.select([F()], [], [], 0.01)

