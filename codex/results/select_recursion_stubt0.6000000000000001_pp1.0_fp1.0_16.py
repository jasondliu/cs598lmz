import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return -1

    select.select([F()], [], [])

    print(a)
    assert a == [1], a
