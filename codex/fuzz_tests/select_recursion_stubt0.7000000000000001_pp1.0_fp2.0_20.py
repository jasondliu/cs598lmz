import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    a.append(F())
    print select.select([], [], [], 1)

test_select_mutated()
