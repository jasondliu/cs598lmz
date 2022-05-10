import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    select.select([], [], [F()], 0)
    a.append(1)
    assert a == [1]

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return -1

    select.select([], [], [F()], 0)
    a.append(1)
    assert a == [1]

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            return -1

    select.select([], [], [F()], 0)
    a.append(1)
    assert a == [1]

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            test_select_mutated4()
            return -1

    select.select([], [], [F()], 0)
    a.append(1)
   
