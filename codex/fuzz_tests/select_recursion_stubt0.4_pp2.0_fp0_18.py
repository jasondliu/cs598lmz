import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    def g():
        a.append(1)
        select.select([F()], [], [], 0)

    g()
    g()

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return len(a)

    def g():
        a.append(1)
        select.select([], [F()], [], 0)

    g()
    g()

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            return len(a)

    def g():
        a.append(1)
        select.select([], [], [F()], 0)

    g()
    g()

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            test_select_mutated4()
            return len(a)

   
