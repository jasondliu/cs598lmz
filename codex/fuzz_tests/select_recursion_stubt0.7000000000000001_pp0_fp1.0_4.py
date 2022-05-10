import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

        def close(self):
            test_select_mutated()

    f1 = F()
    a.append(1)
    f2 = F()
    a.append(2)
    f3 = F()
    a.append(3)
    f4 = F()
    a.append(4)
    f5 = F()

    select.select([f1, f2, f3], [f4, f5], [])
    del f1, f2, f3, f4, f5

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return a.pop()

        def close(self):
            test_select_mutated2()

    f1 = F()
    a.append(1)
    f2 = F()
    a.append(2)
    f3 = F()
    a.append(3)
    f4 = F()
    a.append(4)

