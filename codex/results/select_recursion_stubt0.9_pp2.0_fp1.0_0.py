import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return None

    a.insert(0, F())
    a.append(F())
    b = a[:]

    while b:
        r, w, x = select.select([], b, [], 0)
        b = b[1:] + b[:1]

    select.poll()
    select.select([], [], [])
