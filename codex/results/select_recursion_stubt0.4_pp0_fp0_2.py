import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a.append(f.fileno())
    select.select([f], [f], [f], 0)
    a.append(f.fileno())
    select.select([f], [f], [f], 0)
    a.append(f.fileno())
    select.select([f], [f], [f], 0)

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return a.pop()

    f = F()
    a.append(f.fileno())
    select.select([f], [f], [f], 0)
    a.append(f.fileno())
    select.select([f], [f], [f], 0)
    a.append(f.fileno())
    select.select([f], [f], [f], 0)

def test_select_mutated_3():
    a = []

    class F:
        def fil
