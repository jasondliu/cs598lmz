import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 10

    f = F()
    s = select.select([f], [f], [f], 0)
    assert a == [1]
    assert s == ([f], [f], [f])

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 10

    f = F()
    s = select.select([f], [f], [f], 0)
    assert a == [1]
    assert s == ([f], [f], [f])

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 10

    f = F()
    s = select.select([f], [f], [f], 0)
    assert a == [1]
    assert s == ([f], [f], [f])
    s = select.select([f], [f], [f], 0)
    assert
