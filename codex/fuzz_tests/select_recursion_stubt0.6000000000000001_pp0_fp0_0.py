import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    a.append(F())
    try:
        select.select(a, a, a, 1)
    except ValueError:
        pass
    else:
        assert False, "select.select didn't fail"
