import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def read(self):
            test_select_mutated()
            a.append(1)

    select.select([F()], [], [])
