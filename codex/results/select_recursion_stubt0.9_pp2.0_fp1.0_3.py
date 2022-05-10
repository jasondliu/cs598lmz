import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return int(a.pop())

    def f(s):
        if a:
            b = select.select([F()], [], [])
            a.pop()
        s = s.lower()
        return s, 1

    t = type('', (object,), {'lower': f})

    l = [t(), t(), t(), t()]

    a.append(2)
    b = l.sort(key=t.lower)
    print(l, a)



def test_col():
    a = []
    def g():
        a.append(1)
        yield 1

    def f():
        d = dict(zip(g(), g()))
        d = dict(d)
        return (d, a.pop())

    descrs = [i, g(), f()]
    descrs = sorted(descrs, key=lambda x: x[1] is 1)

    assert(len(descrs) == 1)

test_col()
test_select_mutated()
