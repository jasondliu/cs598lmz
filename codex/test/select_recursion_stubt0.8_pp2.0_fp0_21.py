import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()
    assert select.select([F()], [], [])

def test_select_error():
    import select
    a = []

    class F:
        def fileno(self):
            a.append(self)
            raise OSError()
    f = F()
    raises(OSError, select.select, [f], [], [])
    assert a == [f]
    a = []
    result = select.select([], [f], [])
    assert a == [f]
    assert result == ([], [f], [])
    a = []
    raises(OSError, select.select, [], [f], [f])
    assert a == [f]
