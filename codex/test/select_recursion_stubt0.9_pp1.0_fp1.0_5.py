import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    f = F()
    sel = select.select([f], [], [])
