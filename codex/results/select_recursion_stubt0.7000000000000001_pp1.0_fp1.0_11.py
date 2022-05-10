import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            raise IOError
        def read(self):
            a.append(1)
            return ''

    f = F()
    select.select([f], [], [])
    assert a == [1], a

def test_select_mutated_2():
    import select, sys
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            raise IOError
        def read(self):
            a.append(1)
            return ''

    f = F()
    select.select([f], [], [])
    assert a == [1], a
