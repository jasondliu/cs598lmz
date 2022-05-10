import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a.append(f)
    select.select([f], [], [])

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 1

    f = F()
    a.append(f)
    select.select([f], [], [])

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 1

    f = F()
    a.append(f)
    select.select([f], [], [], 1)

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 1

    f = F()
    a.append(f)
    select.select([f], [], [], 1)

def test_select_mutated5():
    a = []

    class F:
       
