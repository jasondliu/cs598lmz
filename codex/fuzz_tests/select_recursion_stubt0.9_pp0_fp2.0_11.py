import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
    F.keys = {}
    a.append(F)
    try:
        r = select.select([F()], [], [], 1.0)
    finally:
        del a[0]
        del F.keys

def test_select_with_dicts():
    a = dict()
    def f():
        a.popitem()
    f.fileno = f
    f.keys = {}
    d = {f: 1}
    try:
        select.select([f()], [], [], 0.1)
    except KeyError:
        pass
    else:
        assert 0
    if d:
        print d

def test_select_with_arrays():
    a = []
    def f():
        a.pop()
        return len(a)
    try:
        f.keys = {}
        a.append(f)
        select.select([f()], [], [], 0.5)
    finally:
        del f.keys

class TestBytes(unittest.Test
