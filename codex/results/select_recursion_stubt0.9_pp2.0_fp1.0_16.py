import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 4

    fd = F()

    def doit(a=a, fd=fd):
        a[:0] = [fd]
        try:
            sel = select.select(a, a, a, 1)
        except ValueError:
            pass

    doit()

if __name__ == "__main__":
    test_select_mutated()
