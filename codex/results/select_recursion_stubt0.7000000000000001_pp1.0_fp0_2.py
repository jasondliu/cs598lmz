import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    a.append(F())

    try:
        select.select([a[0]], [], [])
    except Exception, e:
        print e

test_select_mutated()
