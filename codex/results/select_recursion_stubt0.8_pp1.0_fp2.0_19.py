import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 3

    def test():
        fd = F()
        a.append(fd)
        return fd

    select.select([test()], a, a)

def test_select_return():
    a = []
    class F:
        def fdopen(self):
            return test_select_return()

    def test():
        fd = F()
        a.append(fd)
        return fd

    fd = test()

    select.select([test()], a, a)

def test_select_resize():
    import _socket
    s = _socket.socket()
    s.connect(('localhost', 10))
    fd = s
    import array
    readfds = [fd]
    writefds = [fd]
    errorfds = [fd]
    readfds = array.array("i", readfds)
    writefds = array.array("i", writefds)
    errorfds = array.array("i", errorfds)
    for i in range(1000):
       
