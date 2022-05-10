import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 4

    select.select([F()], [], [])
    del a[:]

def test_select_err():
    a = []

    class F:
        def fileno(self):
            return 4

