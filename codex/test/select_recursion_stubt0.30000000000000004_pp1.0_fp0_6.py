import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    def f():
        a.append(1)
        select.select([F()], [], [])
        a.append(2)

    f()
    assert a == [1, 2]

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return 0

    def f():
        a.append(1)
        select.select([F()], [], [], 0.1)
        a.append(2)

    f()
    assert a == [1, 2]

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_3()
            return 0

    def f():
        a.append(1)
        select.select([F()], [], [], 0.1, 0.1)
        a.append(2)

    f()
    assert a == [1, 2]

