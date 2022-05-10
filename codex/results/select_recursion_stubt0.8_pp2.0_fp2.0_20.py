import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 42

    for i in range(4):
        a.append(F())
    a.append(sys.stdin)

    r, w, e = select.select(a, [a[0]], a, 1.0)
    print(r, w, e)

test_select_mutated()
