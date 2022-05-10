import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    fd = F()

    a.append(fd)
    select.select([fd], [], [], 0)

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            test_select_closed()
            return a.pop()

    fd = F()

    a.append(fd)
    select.select([fd], [], [], 0)

def test_select_reused():
    a = []

    class F:
        def fileno(self):
            test_select_closed()
            return a.pop()

    fd = F()

    a.append(fd)
    select.select([fd], [], [], 0)

    a.append(fd)
    select.select([fd], [], [], 0)

def test_select_closed_after_select():
    fd = os.open(__file__, os.O_RDONLY)
    select.select([fd], [], [], 0)
    os.close(
