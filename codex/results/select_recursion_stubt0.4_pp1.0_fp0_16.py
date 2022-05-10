import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a.append(1)
    select.select([f], [f], [f], 0)
    a.append(2)
    select.select([f], [f], [f], 0)
    a.append(3)
    select.select([f], [f], [f], 0)

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return a.pop()

    f = F()
    a.append(1)
    select.select([f], [f], [f], 0)
    a.append(2)
    select.select([f], [f], [f], 0)
    a.append(3)
    select.select([f], [f], [f], 0)

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            return a.pop()
