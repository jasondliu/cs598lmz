import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 10

    def g():
        a.append(F())
        return a[0]

    select.select([g()], [], [])

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return 10

    def g():
        a.append(F())
        return a[0]

    select.select([g()], [], [], 1)

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_3()
            return 10

    def g():
        a.append(F())
        return a[0]

    select.select([g()], [], [], 1, 1)

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_4()
            return 10

