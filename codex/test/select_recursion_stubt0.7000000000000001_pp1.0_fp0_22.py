import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0
    a.append(F()) # that's fine

    for f in select.select([], a, []):
        print(f)

test_select_mutated()
