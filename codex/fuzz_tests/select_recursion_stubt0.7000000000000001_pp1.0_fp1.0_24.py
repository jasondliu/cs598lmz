import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            del a[0]
            return 4

    select.select([F()], [], [])
