import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

        def read(self):
            a.append(1)
            return b'A'

    class F2:
        def fileno(self):
            return 2

    class F3:
        def fileno(self):
            return 3

    select.select([F()], [F2()], [F3()], 0)
    assert a == [1]


def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return 1

        def read(self):
            a.append(1)
            return b'A'

    class F2:
        def fileno(self):
            return 2

    class F3:
        def fileno(self):
            return 3

    select.select([F()], [F2()], [F3()], 0)
    assert a == [1]


def test_select_mutated_3():
    a = []

