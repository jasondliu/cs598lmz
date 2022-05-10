import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a[0]
    r, w, e = select.select([F()], [], [])
    assert r == []

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            return a[0]
    r, w, e = select.select([F()], [], [])
    assert r == []

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            a[:] = [1]
            return 0
    r, w, e = select.select([F()], [], [])
    assert r == []

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            a[:] = [1]
            return 0
    r, w, e = select.select([F()], [], [])
    assert r == []

def test_select_mutated5():
    a = []

    class F:
        def fileno(self
