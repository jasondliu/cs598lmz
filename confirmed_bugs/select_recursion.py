import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return self.fileno()

    a[:] = [F()] * 10
    select.select([], a, []), ([], a[:5], [])

test_select_mutated()
