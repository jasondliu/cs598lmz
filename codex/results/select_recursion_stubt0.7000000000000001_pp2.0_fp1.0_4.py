import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            assert False, "shouldn't be called"
            return 0

    f = F()
    a.append(f)
    select.select([f], [f], [f], 0)
    a.remove(f)

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.remove(f)
            return 0

    f = F()
    a.append(f)
    select.select([f], [f], [f], 0)

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            a.append(f)
            return 0

    f = F()
    a.append(f)
    select.select([f], [f], [f], 0)

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 0

    f = F()
    a.append(f)
    select
