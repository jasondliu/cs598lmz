import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    a.append(F())
    select.select(a, a, a)

    def F():
        fd = 1
        fd += 1
        select.select([fd], [], [])

    F()
