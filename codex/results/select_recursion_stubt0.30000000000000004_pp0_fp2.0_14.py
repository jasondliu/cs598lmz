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
            a.append(1)
            return 0

    def f():
        a.append(2)
        select.select([F()], [], [])
        a.append(3)

    f()
    assert a == [2, 1, 3]

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 0

    def f():
        a.append(2)
        select.select([F()], [], [])
        a.append(3)

    f()
    assert a == [2, 1, 3]

def test_select_mutated_4():
    a = []

   
