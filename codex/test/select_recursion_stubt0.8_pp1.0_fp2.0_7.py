import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop(0)

    f = F()
    fd = f.fileno()
    select.select([fd], [], [], 0)
