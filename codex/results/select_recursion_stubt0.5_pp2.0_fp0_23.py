import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    f = F()
    a.append(f)
    select.select([f], [], [], 0)

def test_select_mutated_del():
    a = []

    class F:
        def fileno(self):
            del a[:]
            return len(a)

    f = F()
    a.append(f)
    select.select([f], [], [], 0)

def test_select_mutated_del_2():
    a = []

    class F:
        def fileno(self):
            del a[0]
            return len(a)

    f = F()
    a.append(f)
    select.select([f], [], [], 0)

def test_select_mutated_del_3():
    a = []

    class F:
        def fileno(self):
            del a[1]
            return len(a)

    f = F()
    a.append(f)
    select.select([f], [], [], 0)

