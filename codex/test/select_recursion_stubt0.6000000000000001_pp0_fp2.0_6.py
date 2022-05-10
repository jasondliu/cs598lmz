import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(self)
            return 42

    f = F()
    select.select([f], [f], [f], 0)
    assert a == [f]

def test_select_mutated2():
    a = []
    class F:
        def fileno(self):
            a.append(self)
            return 42

    f = F()
    select.select([f], [f], [f], 0)
    assert len(a) == 1
    assert a[0] is f

def test_select_mutated3():
    a = []
    class F:
        def fileno(self):
            a.append(self)
            return 42

    f = F()
    select.select([f], [f], [f], 0)
    assert len(a) == 1
    assert a[0] is f

def test_select_mutated4():
    a = []
    class F:
        def fileno(self):
            a.append(self)
            return 42

    f = F()
