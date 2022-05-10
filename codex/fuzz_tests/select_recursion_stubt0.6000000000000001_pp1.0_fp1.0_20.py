import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0
    a.append(F())
    test_select_mutated()
    select.select([0], [], [], 0)
    test_select_mutated()

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return 0
    a.append(F())
    test_select_mutated_2()
    select.select([0], [], [], 0)
    test_select_mutated_2()

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_3()
            return 0
    a.append(F())
    test_select_mutated_3()
    select.select([0], [], [], 0)
    test_select_mutated_3()

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            test
