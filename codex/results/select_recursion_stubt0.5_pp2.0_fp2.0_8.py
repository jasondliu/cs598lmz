import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    r = select.select([F()], [], [])
    print(r)

test_select_mutated()
