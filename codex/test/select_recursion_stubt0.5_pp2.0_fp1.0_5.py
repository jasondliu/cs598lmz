import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    a = [F()]
    select.select(a, a, a)

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return len(a)

    a = [F()]
    select.select(a, a, a, 0)

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            return len(a)

    a = [F()]
    select.select(a, a, a, 0.0)

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            test_select_mutated4()
            return len(a)

    a = [F()]
    select.select(a, a, a, 0.0, 0)

def test_select_mutated5():
    a = []

   
