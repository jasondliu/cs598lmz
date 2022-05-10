import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    select.select([], [], [F()])
    a.append(1)

    assert a == [1]

def test_select_bug_1837591():
    class F:
        def fileno(self):
            return 2

    select.select([], [], [F()], 1)
