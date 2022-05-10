import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop().fileno()

    a.append(F())
    a.append(sys.stdin)

    select.select([F()], [], [])

test_select_mutated()
