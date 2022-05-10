import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

        def close(self):
            a.pop()

    a.append(F())
    select.select([], a, [])
    test_select_mutated()


def test_select_mutated_2():
    a = [1]

    class F:
        def fileno(self):
            a.pop()
            return 0

        def close(self):
            pass

    select.select([], [F()], [])
    test_select_mutated_2()


def test_select_mutated_3():
    a = [1]

    class F:
        def fileno(self):
            a.append(None)
            return 0

        def close(self):
            pass

    select.select([], [F()], [])
    test_select_mutated_3()
