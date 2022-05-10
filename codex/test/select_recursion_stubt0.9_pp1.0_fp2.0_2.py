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
