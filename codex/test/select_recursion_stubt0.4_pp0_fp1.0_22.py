import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    f = F()
    a.append(f)
    try:
        select.select([f], [], [])
    except ValueError:
        pass
    else:
        assert False, "expected ValueError"
    a.remove(f)
    try:
        select.select([f], [], [])
    except ValueError:
        assert False, "unexpected ValueError"

test_select_mutated()
