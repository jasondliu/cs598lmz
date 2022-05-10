import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    f1 = F()
    f2 = F()

    a.append(f1)
    a.append(f2)

    select.select([f1], [], [])
