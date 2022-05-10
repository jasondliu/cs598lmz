import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(True)
            return -1

    x = select.select([F()], [], [])
    if len(a) == 0:
        raise Exception("list mutated after select")
