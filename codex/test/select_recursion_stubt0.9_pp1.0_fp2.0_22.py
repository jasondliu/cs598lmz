import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # mutation

        def log(self, val):
            a.append(val)

    F().log(True)
    fileno = F().fileno
    selects = [select.select([fileno], [], [], 0)]
    print(selects)
