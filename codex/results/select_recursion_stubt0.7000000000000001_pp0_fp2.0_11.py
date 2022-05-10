import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 123

    def g():
        a.append(1)

    def h():
        a.append(2)

    select.select([F()], [g], [h])
    assert a == [1, 2]
