import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # recurse
            return a.pop()

    s = select.select([F()], [], [], 0)
    assert s == ([], [], []), s
