import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
    select.select([F()], [], [], 0)

def test_select_mutated2():
    a = []
    class F:
        def fileno(self):
            return len(a)
    select.select([F()], [], [], 0)
    test_select_mutated()
