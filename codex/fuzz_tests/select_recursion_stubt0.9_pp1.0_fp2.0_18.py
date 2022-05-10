import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def close(self):
            a.append("done")

    s = select.select([F()], [], [], 0.1)
    test_support.gc_collect()
    assert a == ["done"], a

def test_kevent_buf():
    import platform
    import errno
    arch = platform.machine()

    from select import kevent

    if arch == 'x86_64':
        KEVENT_SZ = 56
    elif arch == 'ia64':
        KEVENT_SZ = 72
    else:
        KEVENT_SZ = 40
        if sys.platform == 'freebsd4':
            KEVENT_SZ = 44

    buf = '\0' * KEVENT_SZ
    kep = kevent.fromkevent(buf)
    assert kep.ident == 0, 'initial ident != 0'
    kep.ident = 10
    assert kep.ident == 10, 'get/set ident failed'
    kep.ident = -1
    assert kep.ident
