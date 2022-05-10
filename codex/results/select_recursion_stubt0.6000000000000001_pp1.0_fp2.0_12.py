import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    a.append(F())
    a.append(a[0])
    select.select(a,a,a)

def test_select_with_bad_fd():
    class F:
        def fileno(self):
            return 1
        def __del__(self):
            os.close(1)
    a = [F()]
    try:
        select.select(a,a,a)
    except select.error as e:
        assert e[0] == errno.EBADF
    else:
        assert False

def test_select_with_bad_fd_in_list():
    class F:
        def fileno(self):
            return 1
        def __del__(self):
            os.close(1)
    a = [F()]
    try:
        select.select(a,a,a)
    except select.error as e:
        assert e[0] == errno.EBADF
    else:
        assert False

def test_select_with_bad_fd_
