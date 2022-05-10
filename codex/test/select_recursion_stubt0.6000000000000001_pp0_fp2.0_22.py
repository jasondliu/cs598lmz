import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

        def close(self):
            a.append(1)

    f = F()
    select.select([f], [], [])
    assert a == []
    f.close()
    assert a == [1]

def test_select_bad_file():
    class F:
        def fileno(self):
            return "abc"

    f = F()
    py.test.raises(TypeError, select.select, [f], [], [])

def test_select_bad_list():
    py.test.raises(TypeError, select.select, None, None, None)
    py.test.raises(TypeError, select.select, [None], None, None)
    py.test.raises(TypeError, select.select, [1], None, None)
    py.test.raises(TypeError, select.select, [1, None], None, None)
    py.test.raises(TypeError, select.select, [1, "a"], None, None)
