import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    select.select([], [F()], [])

if __name__ == "__main__":
    test_select_mutated()
