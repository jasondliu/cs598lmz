import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0
        def read(self):
            a.append(1)
            return b"x"

    s = select.select([F()], [], [], 0.1)
    gc.collect()
    if a:
        raise Exception("select mutated the object list")

def test_select_closed_fd():
    a = []

    class F:
        def __init__(self, fd):
            self.fd = fd
            a.append(self)
        def fileno(self):
            return self.fd
        def read(self):
            return b"x"

    f = F(0)
    gc.collect()

    s = select.select([f], [], [], 0.1)
    gc.collect()
    if a:
        raise Exception("select mutated the object list")

def test_select_closed_fd_2():
    a = []

    class F:
        def __init__(self, fd):
            self.fd = fd
            a.append(self)
        def
