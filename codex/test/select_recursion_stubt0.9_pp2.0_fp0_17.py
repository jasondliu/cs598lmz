import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            test_select_mutated()
            return a[0]

    class G:
        def fileno(self):
            test_select_mutated()
            test_select_mutated()
            return a[1]

    a = [1, 2]
    i = 0
    while True:
        select.select([F(), G()], [], [])
        if i % 1000 == 0:
            a.append(0)
            a.append(0)
            a[0] += 1
            a[1] += 1
        i += 1

test_select_mutated()
