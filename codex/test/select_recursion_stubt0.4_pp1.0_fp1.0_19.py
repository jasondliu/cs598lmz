import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    select.select([F()], [], [])


def test_select_mutated_2():
    class F:
        def fileno(self):
            return 0

    select.select([F()], [], [])
    test_select_mutated_2()


def test_select_mutated_3():
    class F:
        def fileno(self):
            return 0

    select.select([F()], [], [])
    test_select_mutated_3()


def test_select_mutated_4():
    class F:
        def fileno(self):
            return 0

    select.select([F()], [], [])
    test_select_mutated_4()


def test_select_mutated_5():
    class F:
        def fileno(self):
            return 0

    select.select([F()], [], [])
    test_select_mutated_5()


