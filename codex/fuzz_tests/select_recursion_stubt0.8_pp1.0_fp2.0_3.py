import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 1
    class F2:
        def fileno(self):
            return 2

    f = F()
    f2 = F2()
    fd = f.fileno()
    fd2 = f2.fileno()

    assert select.select([f2],[],[]) == ([f2], [], [])
    assert a == [1]
    assert select.select([f],[],[]) == ([f], [], [])
    assert a == [1]
    assert select.select([],[f2], []) == ([], [f2], [])
    assert a == [1]
    assert select.select([],[f], []) == ([], [f], [])
    assert a == [1]
    assert select.select([f2],[f2], []) == ([f2], [f2], [])
    assert a == [1]
    assert select.select([f],[f], []) == ([f], [f], [])
    assert a == [1]
    assert select.select([],[],[f2
