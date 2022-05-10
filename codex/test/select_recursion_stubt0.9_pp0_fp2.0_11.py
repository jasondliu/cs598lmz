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
