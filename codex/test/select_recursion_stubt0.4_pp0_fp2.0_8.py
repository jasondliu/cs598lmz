import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    f = F()
    a.append(f)
    try:
        select.select([f], [], [])
    except RuntimeError:
        pass
    else:
        raise Exception("didn't crash")
