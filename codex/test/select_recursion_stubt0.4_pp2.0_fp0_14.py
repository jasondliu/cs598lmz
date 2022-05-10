import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a.append(1)
    fd = f.fileno()
    assert fd == 1
    a.append(2)
    fd = f.fileno()
    assert fd == 2
    a.append(3)
    fd = f.fileno()
    assert fd == 3

def test_select_fileno():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    f = F()
    a.append(1)
    fd = f.fileno()
    assert fd == 1
    a.append(2)
    fd = f.fileno()
    assert fd == 2
    a.append(3)
    fd = f.fileno()
    assert fd == 3

def test_select_fileno_exception():
    class F:
        def fileno(self):
            raise ValueError

    f = F()
    raises(ValueError, f.fileno)


