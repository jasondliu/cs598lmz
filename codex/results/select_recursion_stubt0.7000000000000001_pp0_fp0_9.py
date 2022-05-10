import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    select.select([], [F()], a, 0)
    a.append(1)
    select.select([], [F()], a, 0)

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()

    select.select([], [F()], a, 0)
    a.append(1)
    select.select([], [F()], a, 0)

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            test_select_mutated_3()

    select.select([], [F()], a, 0)
    a.append(1)
    select.select([], [F()], a, 0)

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            if a:
                test_select_mutated
