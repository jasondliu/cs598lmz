import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    def f(a=a):
        select.select([F()], [], [])

    try:
        f()
    except IndexError:
        pass

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return a.pop()

    def f(a=a):
        select.select([F()], [], [], 1)

    try:
        f()
    except IndexError:
        pass

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            return a.pop()

    def f(a=a):
        select.select([], [F()], [])

    try:
        f()
    except IndexError:
        pass

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            test_select_mutated
