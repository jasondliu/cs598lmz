import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 2
    f = F()
    a.append(f)
    fd = f.fileno()
    if fd != 2:
        raise test_support.TestFailed("fileno() returned %d, instead of 2" % fd)

def test_select_large_fd():
    try:
        fd = os.open("/dev/null", os.O_RDONLY)
        r = select.select([fd], [], [], 0)
        os.close(fd)
    except select.error, e:
        if e.args[0] != errno.EBADF:
            raise test_support.TestFailed("select.error: %s" % str(e))

def test_select_error():
    try:
        select.select([-1], [], [])
    except select.error, e:
        if e.args[0] != errno.EBADF:
            raise test_support.TestFailed("select.error: %s" % str(e))
    else:
        raise test
