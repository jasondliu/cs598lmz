import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0
        def __del__(self):
            a.append(1)

    f = F()
    try:
        select.select([f], [], [], 0)
    except ValueError:
        pass
    else:
        assert False, "ValueError not raised"
    assert a == [1]

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 0
        def __del__(self):
            a.append(1)

    f = F()
    f.close = lambda: a.append(2)
    try:
        select.select([f], [], [], 0)
    except ValueError:
        pass
    else:
        assert False, "ValueError not raised"
    assert a == [2, 1]

def test_select_closed_mutated():
    a = []

    class F:
        def fileno(self):
            return 0
        def __del__(self):
            a.append(1)

    f = F()

