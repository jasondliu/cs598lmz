import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    a.append(F())
    a.append(F())

    select.select(a, a, a)

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return len(a)

    a.append(F())
    a.append(F())

    select.select(a, a, a, 0.0)

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_3()
            return len(a)

    a.append(F())
    a.append(F())

    select.select(a, a, a, 0.0)
    select.select(a, a, a)

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_4()
            return len(a)
