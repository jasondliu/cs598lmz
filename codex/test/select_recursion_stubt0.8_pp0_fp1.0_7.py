import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

        def read(self):
            pass
    s = select.select([], [], [F()])
    print(s)

# run_test(name='select_mutated')

