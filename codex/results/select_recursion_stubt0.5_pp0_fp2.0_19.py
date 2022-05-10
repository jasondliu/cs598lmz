import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    f = F()
    a.append(f)
    select.select([], [], a)


def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            return 0

    f = F()
    a.append(f)
    select.select([], [], a)
    test_select_mutated2()
