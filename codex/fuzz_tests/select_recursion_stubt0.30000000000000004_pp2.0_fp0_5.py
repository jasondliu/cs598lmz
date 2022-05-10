import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    select.select([F()], [], [])
    test_select_mutated()

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return 1

    select.select([F()], [], [])
    test_select_mutated2()

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            return 1

    select.select([F()], [], [])
    test_select_mutated3()

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            test_select_mutated4()
            return 1

    select.select([F()], [], [])
    test_select_mutated4()

def test_select_mutated5():
    a = []

    class F:
        def fileno(self):
           
