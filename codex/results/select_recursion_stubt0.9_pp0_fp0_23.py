import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(10000)

        def close(self): a.append(1)
        def read(self):  a.append(2)
        def write(self, b):a.append(3)

    select.select(a,a,a,0)
    assert a == []

    r = [F(), F()]
    r.append(F())
    assert a == [10000]

    x = select.select(r,a,a,0)
    for b in r: b.close()
    assert a == [10000, 1, 1, 1, 2, 2, 2]
    for f in x[2]: f.read()
    assert a == [10000, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3]
