import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def read(self):
            a.append(1)
            return b""

    f = F()
    select.select([f], [], [])
    assert a == [1]
