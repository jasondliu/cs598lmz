import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    a.append(F())
    select.select([], a, [])

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 1

    a.append(F())
    select.select([], a, [])
    a[0].close()
    select.select([], a, [])

def test_select_closed_fd():
    a = []

    class F:
        def fileno(self):
            return 1

    a.append(F())
    select.select([], a, [])
    os.close(1)
    select.select([], a, [])

def test_select_closed_fd_2():
    a = []

    class F:
        def fileno(self):
            return 1

    a.append(F())
    select.select([], a, [])
    os.close(1)
    os.close(1)
    select.select([], a, [])

