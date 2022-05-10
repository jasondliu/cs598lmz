import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    def f():
        a.append(5)
        a.append(6)
        select.select([F()], [], [])
    f()
    assert a == [5]

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return 0

    def f():
        a.append(5)
        a.append(6)
        select.select([F()], [], [])
    f()
    assert a == [5]

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_3()
            return 0

    def f():
        a.append(5)
        a.append(6)
        select.select([F()], [], [])
    f()
    assert a == [5]
