import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())
    try:
        select.select([], [], a)
    except ValueError:
        pass
    else:
        assert False, "expected ValueError"

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 0
        def close(self):
            a.append(None)

    a.append(F())
    select.select([], [], a)
    assert a == [None]

def test_select_closed_mutated():
    a = []

    class F:
        def fileno(self):
            return 0
        def close(self):
            a.append(None)

    a.append(F())
    try:
        select.select([], [], a)
    except ValueError:
        pass
    else:
        assert False, "expected ValueError"
    assert a == [None]

def test_select_closed_mutated_2():
    a = []

    class F:
        def fileno
