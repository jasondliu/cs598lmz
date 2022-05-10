import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    with raises(ValueError):
        select.select([F()], [], [])

def test_select_mutated_2():
    f = {}
    def f_pop(x):
        return f.pop(x)

    with raises(ValueError):
        select.select([f_pop(0)], [], [])

def test_select_mutated_3():
    class F:
        def fileno(self):
            return 0

    f = [F() for i in range(10)]

    with raises(ValueError):
        select.select(f, [], [])
    f.pop()
    assert select.select([f[0]], [], [], 0) == ([], [], [])

def test_select_mutated_4():
    class F:
        def fileno(self):
            return 0

    f = [F() for i in range(10)]

    with raises(ValueError):
        select.select(f, [], [], 0)
    f.pop()
   
