import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1
        def close(self):
            a.append(1)

    select.select([F()], [], [])
    assert a == [1]

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return 1
        def close(self):
            a.append(1)

    select.select([], [F()], [])
    assert a == [1]

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_3()
            return 1
        def close(self):
            a.append(1)

    select.select([], [], [F()])
    assert a == [1]

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_4()
            return 1
