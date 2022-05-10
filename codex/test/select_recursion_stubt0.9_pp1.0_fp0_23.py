import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 3

    try:
        select.select([F()], [], [])
    except Exception:
        pass
    test_select_mutated()
    if len(a) == 0:
        raise ValueError()

test_select_mutated()
