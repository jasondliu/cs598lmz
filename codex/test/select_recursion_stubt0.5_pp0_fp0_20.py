import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1
    class F2:
        def fileno(self):
            return 2
    a.append(F2())
    a.append(F())
    a.append(F2())
    select.select(a, a, a, 1)
    assert False

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            return 1
    class F2:
        def fileno(self):
            test_select_mutated2()
            return 2
    a.append(F2())
    a.append(F())
    a.append(F2())
    select.select(a, a, a, 1)
    assert False

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            return 1
    class F2:
        def fileno(self):
            test_select_mutated3()
            return 2
    a.append(F())
    a.append(F2())
