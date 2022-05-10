import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
        def read(self):
            a.append(1)
        def __del__(self):
            a.append(2)

    f = F()

    class MyIOError(IOError):
        pass

    def myselect(rlist, wlist, xlist, timeout=0):
        for i in range(3):
            # This is a kludge to make sure that the file descriptor
            # is not returned by the select() syscall.  I don't know
            # of a portable way to do this, so I'm relying on the
            # internal structure of the select module.
            if len(a) == len(select.epoll.epoll._fdmap):
                raise MyIOError()
        #if len(a) == 1:
        #    raise ValueError()
        return rlist, wlist, xlist

    try:
        with mock.patch('select.select', new=myselect):
            select.select([f], [], [], 0)
    except MyIOError:
        pass
    assert a ==
