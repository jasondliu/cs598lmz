import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 9

    class F2:
        def fileno(self):
            a.append(1)
            return 10

    select.select([F(), F2()], [], [], [F()])
    assert len(a) == 2
