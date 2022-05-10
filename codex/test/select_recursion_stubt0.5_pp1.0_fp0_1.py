import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    a.append(F())

    try:
        select.select([], [], [])
    except ValueError:
        pass
    else:
        assert False, "select() should raise ValueError"
