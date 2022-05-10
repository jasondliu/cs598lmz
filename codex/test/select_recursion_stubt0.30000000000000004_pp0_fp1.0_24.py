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
        assert False, "select() didn't raise ValueError"

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 0

        def close(self):
            a.append(1)

    f = F()
    a.append(f)
    try:
        select.select([f], [], [])
    except ValueError:
        pass
    else:
        assert False, "select() didn't raise ValueError"
    assert a == [f, 1]

def test_select_closed_pipe():
    a = []

    class F:
        def fileno(self):
            return 0

        def close(self):
            a.append(1)

    f = F()
    a.append(f)
