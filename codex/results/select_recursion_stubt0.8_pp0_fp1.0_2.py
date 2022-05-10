import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            if a:
                return a.pop()
            raise ValueError

        def close(self):
            pass

    s = select.select([F()], [], [])
