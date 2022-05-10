import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
    f = F()
    a.append(0)
    select.select([f], [f], [f], 0)

test_select_mutated()
