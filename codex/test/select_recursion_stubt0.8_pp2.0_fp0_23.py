import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

        def close(self):
            del a[0]

    a.append(F())
