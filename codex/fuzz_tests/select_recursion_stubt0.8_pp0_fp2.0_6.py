import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    f = F()

    try:
        select.select([], [], [f])
    except select.error, err:
        # XXX could check that err.args[0] is EBADF
        pass
    else:
        assert False, "select should raise"

    assert not a

def test_select_bad_fd():
    class F:
        def fileno(self):
            return -1

    f = F()

    try:
        select.select([], [f], [])
    except select.error, err:
        # XXX could check that err.args[0] is EBADF
        pass
    else:
        assert False, "select should raise"

def test_select_interrupt():
    class F:
        def fileno(self):
            return -1

    a = []

    def handler(*args):
        a.append(1)

    f = F()
    oldby = signal.signal(signal.SIGALRM, handler)
    signal.alarm(1)
    try:
