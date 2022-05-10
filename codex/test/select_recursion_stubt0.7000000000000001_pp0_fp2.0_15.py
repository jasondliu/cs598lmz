import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 0

    f = F()
    select.select([f], [], [], 0.1)
