import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    a.append(F())
    try:
        select.select([], [], [])
    except ValueError:
        pass
    else:
        assert False, "no ValueError raised"

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return len(a)

    a.append(F())
    del a[0]
    try:
        select.select([], [], [])
    except ValueError:
        pass
    else:
        assert False, "no ValueError raised"

def test_select_closed_mutated():
    a = []

    class F:
        def fileno(self):
            del a[0]
            return len(a)

    a.append(F())
    try:
        select.select([], [], [])
    except ValueError:
        pass
    else:
        assert False, "no ValueError raised"
