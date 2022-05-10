import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    f = F()
    a.append(f)
    f.fileno()
    select.select([f], [], [])

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            return len(a)

    f = F()
    a.append(f)
    f.fileno()
    select.select([f], [], [])

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            return len(a)

    f = F()
    a.append(f)
    f.fileno()
    select.select([f], [], [])

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            return len(a)

    f = F()
    a.append(f)
    f.fileno()
    select.select([f], [], [])

def test_select_mut
