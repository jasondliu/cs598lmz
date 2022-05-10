import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
    f = F()
    select([f], [], [])
    a.append(1)
    select([f], [], [])

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return len(a) - 1
    f = F()
    select.select([f], [], [])
    select.select([f], [], [])
    select.select([f], [], [])

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            if len(a) == 2:
                test_select_mutated_3()
            a.append(1)
            return len(a) - 1
    f = F()
    select.select([f], [], [])
    select.select([f], [], [])
    select.select([f], [], [])

def test_select_mutated_4():
    a
