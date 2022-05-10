import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(self)
            return 0

    select.select([F()], [], [])
    assert a == [a[0]]

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            a.append(self)
            return 0

    select.select([], [F()], [])
    assert a == [a[0]]

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_3()
            a.append(self)
            return 0

    select.select([], [], [F()])
    assert a == [a[0]]

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_4()
            a.append(self)
            return 0

    select.select([F()], [F()], [])
