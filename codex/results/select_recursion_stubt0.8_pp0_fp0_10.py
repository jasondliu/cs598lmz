import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 3

        def close(self):
            a.append(2)

    f = F()
    def r():
        select.select([f], [], [], 0.0)

    r()
    assert a == [1,2]
