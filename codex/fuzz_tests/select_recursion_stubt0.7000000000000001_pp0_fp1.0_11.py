import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a[-1])

    f = F()
    a.append([f])
    s = select.select([f], [], [])
    assert s == ([f], [], [])
    a[-1].remove(f)

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            return len(a[-1])

    f = F()
    a.append([f])
    s = select.select([f], [], [])
    assert s == ([], [], [])
    a[-1].remove(f)

def test_select_third_argument_type():
    import _testcapi
    raises(TypeError, select.select, [], [], 1)
    raises(TypeError, select.select, [], [], None)
    raises(TypeError, select.select, [], [], "")
    raises(TypeError, select.select, [], [], ())
    raises(TypeError, select.select, [], [], [])

