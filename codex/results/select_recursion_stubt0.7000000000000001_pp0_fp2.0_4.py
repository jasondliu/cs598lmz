import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            raise ValueError
    a.append(F())

    def f():
        select.select([], a, a)
    raises(ValueError, f)

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            raise TypeError
    a.append(F())

    def f():
        select.select([], a, a)
    raises(TypeError, f)

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            raise ValueError
    a.append(F())

    def f():
        select.select([a], a, a)
    raises(ValueError, f)
