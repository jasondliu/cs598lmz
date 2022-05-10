import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    select.select([F()], a, a, 1)

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return 1

    select.select([], a, a, 1)

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_3()
            return 1

    select.select([], [], a, 1)

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_4()
            return 1

    select.select([], [], [], 1)

def test_select_mutated_5():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_5()
            return 1

    select.select([], [], [], 1)

def test
