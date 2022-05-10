import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())
    try:
        select.select(a, [], [])
    except RuntimeError:
        pass

def test_select_large_fd():
    a = []

    class F:
        def fileno(self):
            return sys.maxsize

    a.append(F())
    try:
        select.select(a, [], [])
    except RuntimeError:
        pass

def test_select_closed_fd():
    a = []

    class F:
        def fileno(self):
            return 0

    a.append(F())
    try:
        select.select(a, [], [])
    except RuntimeError:
        pass

def test_select_closed_pipe():
    a = []

    class F:
        def fileno(self):
            return os.pipe()[0]

    a.append(F())
    try:
        select.select(a, [], [])
    except RuntimeError:
        pass

