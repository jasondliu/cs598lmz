import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    f = F()
    a.append(f)
    select.select([f], [], [])

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            return len(a)

    f = F()
    a.append(f)
    select.select([f], [], [])
    test_select_mutated()

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            return len(a)

    f = F()
    a.append(f)
    select.select([f], [], [])
    a.pop()

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            return len(a)

    f = F()
    a.append(f)
    select.select([f], [], [])
    a.pop()
    test_select_mutated()

def
