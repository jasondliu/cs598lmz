import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0
    a.append(F())
    try:
        select.select(a,a,a,0)
    except select.error, e:
        assert e.args[0] == errno.EINTR
    else:
        assert 0, "select.error not raised"

def test_select_bogus_fd():
    import sys
    import _minimal_c_lib
    if sys.platform == "win32":
        import msvcrt
        fd = msvcrt.open_osfhandle(0, os.O_RDONLY)
    else:
        fd = _minimal_c_lib.open("/dev/null", os.O_RDONLY)
    try:
        select.select([fd], [], [], 0)
    except select.error, e:
        assert e.args[0] == errno.EBADF
    else:
        assert 0, "select.error not raised"
