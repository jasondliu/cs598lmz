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
    except ValueError:
        pass
    else:
        assert False, "select() didn't raise ValueError"

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return len(a)

    f = F()
    a.append(f)
    a.append(f)
    a.append(f)
    a.append(f)
    a.append(f)
    a.append(f)
    a.append(f)
    a.append(f)
    a.append(f)
    a.append(f)
    a.append(f)
    a.append(f)
    a.append(f)
    a.append(f)
    a.append(f)
    a.append(f)
    a.append(f)
    a.append(f)
