import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    def f():
        select.select([F()], [], [], 0)

    def g():
        a.append(1)
        f()

    g()

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return 0

    def f():
        select.select([F()], [], [], 0)

    def g():
        a.append(1)
        f()

    def h():
        a.append(1)
        g()

    h()

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_3()
            return 0

    def f():
        select.select([F()], [], [], 0)

    def g():
        a.append(1)
        f()

    def h():
        a.append(1)
        g()

    def i():
        a
