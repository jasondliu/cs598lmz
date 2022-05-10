import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 42
    a.append(F())
    select.select(a, [], [])

class F:
    n = 42

    def fileno(self):
        return F.n

    def close(self):
        F.n = 24

def test_select_close():
    a = []
    a.append(F())
    select.select(a, [], [])
    assert F.n == 24

class B:
    def fileno(self):
        return 42

class D(B):
    pass

def test_select_inherit():
    assert select.select([D()], [], [], 1.0) == ([B()], [], [])
