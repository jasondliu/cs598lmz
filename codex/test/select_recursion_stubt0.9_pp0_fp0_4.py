import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()  # unintended side-effect
            return len(a)

        def read(self):
            return a.pop()

    reader = F()
    a = [reader]
    select.select([reader], [], [], 0.1)
