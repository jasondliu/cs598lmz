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
        select.select(a, a, a)
    except ValueError:
        pass
    else:
        assert False, "select() didn't fail"

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 0

        def close(self):
            a.append(None)

    f = F()
    a.append(f)
    select.select(a, a, a)
    assert a == [None, None], "select() didn't close"

def test_select_closed_mutated():
    a = []

    class F:
        def fileno(self):
            return 0

        def close(self):
            test_select_closed_mutated()

    f = F()
    a.append(f)
    try:
        select.select(a, a, a)
    except ValueError:
        pass
    else:
        assert False, "select() didn't fail"
