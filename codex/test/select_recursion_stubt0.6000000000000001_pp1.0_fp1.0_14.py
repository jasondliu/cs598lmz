import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 3

        def read(self):
            pass

    a.append(F())

    select.select(a, [], [], 0.1)

test_select_mutated()
