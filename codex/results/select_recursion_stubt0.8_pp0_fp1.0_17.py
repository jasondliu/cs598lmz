import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(F())
            return 0

        def close(self):
            print("do nothing")

    selector = select.select([F()], [], [])
    assert selector == ([], [], []), selector
    assert len(a) == 0

def test_select_mutated_again():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_again()
            a.append(F())
            return 0

        def close(self):
            print("do nothing")

    selector = select.select([F()], [], [], 0)
    assert selector == ([], [], []), selector
    assert len(a) == 0

def test_select_mutated_timeout():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_timeout()
            a.append(F())
            return 0

        def close(self):
            print("do nothing")

    selector = select.select([F()], [], [], 10)
    assert selector
