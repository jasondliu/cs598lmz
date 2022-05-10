import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    f = F()
    select.select([f], [], [])
    assert a == [1]

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            test_select_mutated_2()

    f = F()
    select.select([f], [], [])
    assert a == [1]

def test_select_mutated_3():
    a = []

    def f():
        a.append(1)
        test_select_mutated_2()

    select.select([f], [], [], 0)
    assert a == [1]

def test_select_mutated_4():
    a = []

    def f():
        a.append(1)
        test_select_mutated()

    select.select([f], [], [], 0)
    assert a == [1]

def test_select_mutated_5():
    a = []

    def f():
