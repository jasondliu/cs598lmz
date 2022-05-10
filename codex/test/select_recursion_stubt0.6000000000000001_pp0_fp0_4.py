import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
    f = F()
    a.append(f)
    try:
        select.select([f], [], [])
    except RuntimeError as e:
        assert str(e) == 'file descriptor cannot be a negative integer (-1)'

class TestSelectError(Exception):
    pass

class TestSelect(object):
    def test_error_conditions(self):
        raises(TypeError, select.select, 1, 2, 3)
        raises(TypeError, select.select, [1], 2, 3)
        raises(TypeError, select.select, [1], [2], 3)
        raises(TypeError, select.select, [1], [2], [3], 4)
        if not hasattr(__import__(os.name), 'pipe'):
            skip("os.pipe not available on this platform")
        r, w = os.pipe()
