import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
        def __enter__(self):
            return self
        def __exit__(self, *args):
            pass

    a.append(F())
    a.append(F())

    select.select(a, [], [])
