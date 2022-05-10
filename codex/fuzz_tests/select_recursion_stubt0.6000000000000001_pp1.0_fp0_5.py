import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], a, a, 0)


def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            return 0

    select.select([F()], a, a, 0)


def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            return 0

    select.select([F()], a, a, 0)
    test_select_mutated_2()


def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            return 0

    select.select([F()], a, a, 0)
    test_select_mutated_3()


def test_select_mutated_5():
    a = []

    class F:
        def fileno(self):
            return 0

    select.select([F()], a, a, 0)
    test_select_mutated_4()


def test_select_
