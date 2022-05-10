import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    f = F()
    a.append(f)

    select.select([], [], a)
    del a[:]

if __name__ == "__main__":
    test_select_mutated()
