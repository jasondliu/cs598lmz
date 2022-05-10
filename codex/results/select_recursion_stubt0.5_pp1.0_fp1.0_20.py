import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())
    select.select([], a, [])

def test_select_large_fd():
    a = []
    for i in range(10):
        class F:
            def fileno(self):
                return i
        a.append(F())

    select.select([], a, [])

def test_select_large_fd_mutated():
    a = []
    for i in range(10):
        class F:
            def fileno(self):
                if i == 5:
                    test_select_large_fd_mutated()
                return i
        a.append(F())

    select.select([], a, [])

def test_select_large_fd_mutated_in_loop():
    a = []
    for i in range(10):
        class F:
            def fileno(self):
                if i == 5:
                    test_select_large_fd_mutated_in_loop()
                return i
        a.append(F())

    for i in range
