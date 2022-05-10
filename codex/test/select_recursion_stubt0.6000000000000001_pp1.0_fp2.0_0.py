import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())

    for i in range(10000):
        try:
            r, w, x = select.select([], [], [])
        except ValueError:
            pass

def test_select_closed_fd():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    a.append(0)
    a.append(1)

    for i in range(10000):
        try:
            r, w, x = select.select([], [], [])
        except ValueError:
            pass

def test_select_closed_pipe():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    r, w = os.pipe()
    a.append(r)
    a.append(w)

    for i in range(10000):
        try:
            r, w, x = select.select([], [], [])
        except ValueError:
            pass

