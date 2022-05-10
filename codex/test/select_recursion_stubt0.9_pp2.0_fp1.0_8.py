import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0
        def copy(self):
            a.append(self)
            return self

    f = F()
    fd = f.fileno()

    select.select([f], [], [])
