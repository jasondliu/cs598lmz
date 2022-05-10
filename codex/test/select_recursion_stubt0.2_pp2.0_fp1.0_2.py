import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())

    try:
        select.select(a, a, a)
    except ValueError:
        pass

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 0

        def close(self):
            a.pop()

    a.append(F())

    try:
        select.select(a, a, a)
    except ValueError:
        pass

def test_select_closed_fd():
    a = []

    class F:
        def fileno(self):
            return 0

        def close(self):
            os.close(0)

    a.append(F())

    try:
        select.select(a, a, a)
    except ValueError:
        pass

def test_select_closed_fd_2():
    a = []

    class F:
        def fileno(self):
            return 0

        def close(self):
            os.close(0)

    a.append(F())

   
