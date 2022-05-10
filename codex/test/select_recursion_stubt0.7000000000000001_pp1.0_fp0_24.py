import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    a.append(F())
    select.select(a, [], [], 1)

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()

    a.append(F())
    select.select(a, [], [], 1)

    a.append(F())
    select.select(a, [], [], 1)

def test_select_mutated_3():
    a = []
    b = []

    class F:
        def fileno(self):
            test_select_mutated_3()

    a.append(F())
    select.select(a, b, [], 1)

    a.append(F())
    select.select(a, b, [], 1)
