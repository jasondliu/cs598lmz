import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    select.select([F()], [], [])

def test_select_mutated2():
    a = []
    def f():
        test_select_mutated2()
        return len(a)

    select.select([f], [], [])

def test_select_mutated3():
    a = []
    def f():
        test_select_mutated3()
        return len(a)

    select.select([f], [], [])

def test_select_mutated4():
    a = []
    def f():
        test_select_mutated4()
        return len(a)

    select.select([f], [], [])

def test_select_mutated5():
    a = []
    def f():
        test_select_mutated5()
        return len(a)

    select.select([f], [], [])

def test_select_mutated6():
    a = []
    def f():
        test_select_mutated6()
        return len
