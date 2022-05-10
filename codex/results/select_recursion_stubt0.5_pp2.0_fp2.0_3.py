import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    a.append(F())
    select.select(a, a, a)

class Foo(object):
    def __init__(self):
        self.r = select.select([self], [], [])

    def fileno(self):
        return self.r[0][0].fileno()

def test_select_mutated2():
    a = Foo()

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            return 1

    a.append(F())
    select.select([], a, a)

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            test_select_mutated4()
            return 1

    a.append(F())
    select.select([], a, a, 1)
