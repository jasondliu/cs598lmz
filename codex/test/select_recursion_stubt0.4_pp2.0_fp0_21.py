import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    a.append(F())
    select.select([a[0]], [], [])
    del a[:]

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return len(a)

    a.append(F())
    select.select([a[0]], [], [], 0.01)
    del a[:]

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_3()
            return len(a)

    a.append(F())
    select.select([a[0]], [], [], 0)
    del a[:]

def test_select_mutated_4():
    import os
    a = []

    class F:
        def fileno(self):
            test_select_mutated_4()
            return len(a)

