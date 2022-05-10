import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [], [])

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    f = F()
    select.select([f], [], [])
    test_select_mutated()

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    f = F()
    select.select([f], [], [])
    test_select_mutated_2()

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    f = F()
    select.select([f], [], [])
    test_select_mutated_3()

def test_select_mutated_5():
    a = []

    class F:
        def fileno(self):
            return a.pop()

   
