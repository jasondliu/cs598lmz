import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()
    select.select([F()], [], [])

def test_select_error():
    class F:
        def fileno(self):
            raise ValueError()
    select.select([F()], [], [])
