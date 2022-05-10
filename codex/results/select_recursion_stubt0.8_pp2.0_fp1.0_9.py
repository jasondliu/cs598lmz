import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    f1 = f.fileno()
    a.append(f1+1)
    # expect exception
    select.select([f], [], [], 0)
