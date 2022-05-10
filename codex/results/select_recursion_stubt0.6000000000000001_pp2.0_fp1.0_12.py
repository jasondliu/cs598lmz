import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a[0]

    f = F()
    a.append(f)
    select.select([f], [], [], 1)

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            del a[:]
            return a[0]

    f = F()
    a.append(f)
    select.select([f], [], [], 1)

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            a[:] = []
            return a[0]

    f = F()
    a.append(f)
    select.select([f], [], [], 1)

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            a[:] = [1, 2, 3]
            return a[0]

    f = F()
    a.append(f)
    select.select([f], [], [], 1
