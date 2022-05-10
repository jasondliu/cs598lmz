import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()   ### the mutation here breaks select.poll

    class G:
        def fileno(self):
            a.append(None)
            raise OSError
    p = select.poll()
    x = G()
    y = F()
    p.register(x,1)
    p.register(y,1)
    assert len(a) == 0
    try:
        p.poll()
    except TypeError:
        pass
    assert len(a) == 0    # should not have called x.fileno()
    try:
        p.poll()
    except TypeError:
        pass
    assert len(a) == 0    # the fileno() should not have been called again for x

def test_select():
    pipe = os.pipe()
    fds = []
    for fd in pipe:
        f = select.fromfd(fd, select.POLLIN)
        fds.append(f)
    l = select.poll()
    l.register(fds[0])
    l.register(fds[1])
    c
