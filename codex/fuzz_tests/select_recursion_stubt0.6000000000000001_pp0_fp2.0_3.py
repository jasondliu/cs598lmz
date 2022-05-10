import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

        def close(self):
            a.append(None)

    s = select.select([F()], [], [])
