import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 5

    a.append(F())

    try:
        select.select([], a, [])
    except RuntimeError:
        pass

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 5

        def close(self):
            a.append(None)

    a.append(F())

    try:
        select.select([], a, [])
    except RuntimeError:
        pass
    assert len(a) == 0

def test_select_closed_2():
    a = []

    class F:
        def fileno(self):
            return 5

        def close(self):
            a.append(None)

    a.append(F())

    try:
        select.select([], a, [])
    except RuntimeError:
        pass
    assert len(a) == 0

def test_select_closed_3():
    a = []

    class F:
        def fileno(self):
            return 5

        def close(self):
            a
