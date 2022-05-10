import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    r = select.select([0, F()], [], [], 0)
    print(r)

test_select_mutated()

def test_select_mutated_2():
    a = []
    class F:
        def fileno(self):
            return a.pop()

    r = select.select([F()], [], [], 0)
    print(r)

test_select_mutated_2()

def test_select_mutated_3():
    a = []
    class F:
        def fileno(self):
            return a.pop()

    r = select.select([0, F()], [], [], 0)
    print(r)

test_select_mutated_3()

def test_select_mutated_4():
    a = []
    class F:
        def fileno(self):
            return a.pop()

    r = select.select([F()], [], [], 0)
    print(r)

test_select_mutated_4
