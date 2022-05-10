import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    a.append(F())
    select.select(a, a, a)

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.pop()

    a.append(F())
    select.select(a, a, a)

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            a.pop()

    a.append(F())
    select.select(a, a, a, 1)

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            a.pop()

    a.append(F())
    select.select(a, a, a, 1.0)
