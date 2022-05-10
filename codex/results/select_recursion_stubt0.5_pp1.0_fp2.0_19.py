import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # mutate the list
            return 1

    a.append(F())
    select.select([], [], a, 1)
