import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    a.append(F())

    while a:
        select.select(a, a, a)
        test_select_mutated()
        a.pop()

def test_select_epoll():
    a = []

    class F:
        def fileno(self):
            test_select_epoll()
            return -1

    a.append(F())

    while a:
        select.epoll(a)
        test_select_epoll()
        a.pop()

def test_select_kqueue():
    a = []

    class F:
        def fileno(self):
            test_select_kqueue()
            return -1

    a.append(F())

    while a:
        select.kqueue(a)
        test_select_kqueue()
        a.pop()
