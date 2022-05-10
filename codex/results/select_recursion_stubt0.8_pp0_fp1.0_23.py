import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # mutated a
            return a[1]

    select.select([F()], [], [])
