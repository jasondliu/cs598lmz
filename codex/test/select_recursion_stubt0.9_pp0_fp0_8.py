import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated(); return 0
    f = F()
    d = {f: a, 1: [2], 3: [4]}
