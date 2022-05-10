import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], [], [], 0)
    a.append(1)
    select.select([], [], [], 0)
    a.append(2)
    select.select([], [], [], 0)
    a.append(3)
    assert a == [1, 2, 3]

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return 0

    select.select([F()], [], [], 0)
    a.append(1)
    select.select([], [], [], 0)
    a.append(2)
    select.select([], [], [], 0)
    a.append(3)
    assert a == [1, 2, 3]

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_3()
            return 0

    select.select([F
