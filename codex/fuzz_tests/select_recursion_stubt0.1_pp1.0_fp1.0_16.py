import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], [], [])
    a.append(1)
    select.select([], [], [])
    a.append(2)
    select.select([], [], [])
    a.append(3)
    assert a == [1, 2, 3]

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return 0

    select.select([F()], [], [])
    a.append(1)
    select.select([], [], [])
    a.append(2)
    select.select([], [], [])
    a.append(3)
    assert a == [1, 2, 3]

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            return 0

    select.select([F()], [], [])
    a.append(1)
   
