import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            b = len(a)
            a.append(1)
            return b
    select.select([F()], [], [])

class F(object):
    def f(self, name):
        return getattr(self, name)

def test_select_mutated2():
    f = F()
    f.fileno = lambda: test_select_mutated2()
    select.select([f], [], [])

def test_select_mutated3():
    f = F()
    f.fileno = lambda: test_select_mutated3()
    select.select([f], [], [])

def test_select_mutated4():
    class F(object):
        def fileno(self):
            test_select_mutated4()
            return 0
    select.select([F()], [], [])

def test_select_mutated5():
    a = []
    class F(object):
        def fileno(self):
            test_select_mutated5()
            b = len(a)
           
