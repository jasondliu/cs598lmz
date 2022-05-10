import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], [F()], [F()], 0)

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 0

    select.select([F()], [F()], [F()], 0)
    test_select_mutated_2()

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 0

    select.select([F()], [F()], [F()], 0)
    a.append(1)
    test_select_mutated_3()

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 0

    select.select([F()], [F()], [F()], 0)
    a.append(1)
    a.append(1)
    test
