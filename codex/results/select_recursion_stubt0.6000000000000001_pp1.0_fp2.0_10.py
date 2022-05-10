import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1
        def recv(self, *args):
            return None

    for i in range(1000):
        a.append(F())

    select.select(a, [], [])

test_select_mutated()
