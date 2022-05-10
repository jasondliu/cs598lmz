import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a[0]

    f = F()
    f.fileno()

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            a.append(0)
            return 0

    f = F()
    f.fileno()
    select.select([f], [], [])

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            a.append(0)
            return 0

    f = F()
    f.fileno()
    select.poll()
    select.poll().register(f)

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            a.append(0)
            return 0

    f = F()
    select.poll()
    select.poll().register(f)
    f.fileno()

def test_select_mutated5():
    a = []

    class F:
        def fileno(self):
