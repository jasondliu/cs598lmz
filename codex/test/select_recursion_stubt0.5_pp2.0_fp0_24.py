import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    f.fileno()
    a.append(1)

    select.select([f], [], [])
