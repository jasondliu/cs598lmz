import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    def f(x):
        a.append(x)

    select.select([F()], [], [], 0)
    f(a)

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return 1

    def f(x):
        a.append(x)

    select.select([F()], [], [], 0)
    f(a)

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_3()
            return 1

    def f(x):
        a.append(x)

    select.select([F()], [], [], 0)
    f(a)

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_4()
            return 1

    def f(x):

