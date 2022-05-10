import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    select.select([F()], [], [])
    test_select_mutated()

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 1

    select.select([F()], [], [])
    test_select_mutated_2()

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 1

    select.select([F()], [], [])
    assert a == [1]
    test_select_mutated_3()

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 1

    select.select([F()], [], [])
    assert a == [1]

def test_select_mutated_5():
    a = []

