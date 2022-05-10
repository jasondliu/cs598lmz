import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return -1

    f = F()
    select.select([f], [], [])
    assert a == [1]

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return -1

    f = F()
    select.select([f], [], [])
    assert a == [1]

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return -1

    f = F()
    select.select([f], [], [], 0)
    assert a == [1]

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return -1

    f = F()
    select.select([f], [], [], 0.1)
    assert a == [1]

