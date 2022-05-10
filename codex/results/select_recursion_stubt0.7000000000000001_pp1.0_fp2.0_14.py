import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    select.select([F()], a, a, 1)

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            del a[0]
            return 1

    select.select([F()], a, a, 1)

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            a[0:0] = a
            return 1

    select.select([F()], a, a, 1)

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            a[0:0] = [1,2,3]
            return 1

    select.select([F()], a, a, 1)

def test_select_mutated_5():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 1

    select.select([F()], a, a, 1)

