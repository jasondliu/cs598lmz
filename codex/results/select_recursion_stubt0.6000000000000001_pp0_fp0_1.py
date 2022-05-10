import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1
    a.append(F())

    class F:
        def fileno(self):
            return 2
    a.append(F())

    b = select.select(a, [], [], 0)
    assert len(b) == 3
    assert len(b[0]) == 1
    assert b[0][0].fileno() == 2

def test_select_closed():
    class F:
        def fileno(self):
            return 1
    f = F()
    f.fileno()
    f.close()
    raises(ValueError, f.fileno)

    b = select.select([f], [], [], 0)
    assert len(b) == 3
    assert len(b[0]) == 0

def test_select_return_list():
    a = []

    class F:
        def fileno(self):
            return 1
    a.append(F())

    class F:
        def fileno(self):
            return 2
    a.append(F())

    b = select.select(a
