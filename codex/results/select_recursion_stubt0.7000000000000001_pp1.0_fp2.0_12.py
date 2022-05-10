import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    class X:
        def __del__(self):
            del a[:]

    a.append(F())
    a.append(X())
    a.append(X())
    a.append(X())

    try:
        select.select(a,a,a)
    except ValueError:
        pass

def test_select_mutated_2():
    a = []
    a.append([])
    a.append([])
    a.append([])
    a.append([])

    try:
        select.select(a[0],a[1],a[2], a[3])
    except ValueError:
        pass


if __name__ == '__main__':
    test_select_mutated()
    test_select_mutated_2()
