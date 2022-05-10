import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
    f = F()

    class F2:
        def fileno(self):
            global a
            a = []
            return 5
    f2 = F2()

    a.append(f)
    select.select([f, f2], [], [], 5)
