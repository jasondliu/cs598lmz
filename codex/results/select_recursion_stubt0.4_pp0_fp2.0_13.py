import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    fd = f.fileno()
    try:
        select.select([f], [], [])
    except ValueError:
        pass
