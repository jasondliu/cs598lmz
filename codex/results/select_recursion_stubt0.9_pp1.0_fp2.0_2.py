import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([], [], [F()], 0)
    a[:] = [1]

def test_time_mutated():
    a = []

    class F:
        def fileno(self):
            test_time_mutated()
            return 0

    open("x", "r")
    a[:] = [1]

def test_bool_mutated():
    a = []

    class F:
        def __nonzero__(self):
            test_bool_mutated()
            return False
    f = F()
    if f:
        raise AssertionError, "should not happen"
    a[:] = [1]

def test_del_mutated():
    a = []

    class A:
        pass
    aa = A()
    del aa.x
    a[:] = [1]

def test_iter_mutated():
    a = []
    list(a)
    a[:] = [1]

def test_oct_mutated():
    a = []


