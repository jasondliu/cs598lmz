import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    def f():
        a.append(1)

    select.select([F()], [], [], 1)
    f()
    assert a == []

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return 0

    def f():
        a.append(1)

    select.select([], [F()], [], 1)
    f()
    assert a == []

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_3()
            return 0

    def f():
        a.append(1)

    select.select([], [], [F()], 1)
    f()
    assert a == []
