import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def read(self, n):
            a.append(1)
            return "a"

    assert select.select([F()], [], []) == ([], [], [])
    assert a == [1]

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            return 0

        def read(self, n):
            a.append(1)
            raise OSError()

    assert select.select([F()], [], []) == ([], [], [])
    assert a == [1]
