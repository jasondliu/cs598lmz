import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 2
        def read(self):
            pass
        def write(self, s):
            pass

    def f():
        a.append(1)

    fd = F()
    a.append(fd)
    select.select([fd], [], [], 1)
    lltype.free(fd, flavor='raw')

    f()
    for i in range(100):
        f()
    for i in range(100):
        f()
    for i in range(100):
        f()
    for i in range(100):
        f()
