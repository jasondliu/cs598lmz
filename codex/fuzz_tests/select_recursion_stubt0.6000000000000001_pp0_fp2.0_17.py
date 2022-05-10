import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    class B:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    a = [3, 5]
    select.select([F(), B()], [], [], 0)

def test_select_too_high_fd():
    a = []

    class F:
        def fileno(self):
            test_select_too_high_fd()
            return a.pop() + 100

    class B:
        def fileno(self):
            test_select_too_high_fd()
            return a.pop() + 100

    a = [3, 5]
    select.select([F(), B()], [], [], 0)
