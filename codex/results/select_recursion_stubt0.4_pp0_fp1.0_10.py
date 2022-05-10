import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1
    f = F()
    a.append(f)
    select.select([f], [], [], 0)
    a.remove(f)
    select.select([f], [], [], 0)

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return 1
    f = F()
    a.append(f)
    select.select([f], [], [], 0)
    a.remove(f)
    select.select([f], [], [], 0)

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_3()
            return 1
    f = F()
    a.append(f)
    select.select([f], [], [], 0)
    a.remove(f)
    select.select([f], [], [], 0)

def test_select_mutated_4
