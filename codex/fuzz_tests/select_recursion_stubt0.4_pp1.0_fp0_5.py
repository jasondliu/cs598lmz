import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [], [], 0)

def test_select_interrupted():
    a = []

    class F:
        def fileno(self):
            test_select_interrupted()
            return a.pop()

    select.select([F()], [], [], 0)

def test_select_interrupted_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_interrupted_mutated()
            return a.pop()

    select.select([F()], [], [], 0)

def test_select_interrupted_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_interrupted_mutated_2()
            return a.pop()

    select.select([F()], [], [], 0)

def test_select_interrupted_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_interrupted_mutated_3()

