import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    f = F()
    a.append(f)

    for i in range(4):
        try:
            select.select(a, [], [])
        except RuntimeError as e:
            print(e)
            if i == 3:
                raise

test_select_mutated()
