import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [], [])

def _test_select_mutated_error(a):
    class F:
        def fileno(self):
            test_select_mutated_error(a)
            return a.pop()

    select.select([F()], [], [])

def test_select_mutated_error():
    a = []
    _test_select_mutated_error(a)


def test_select_double_wrap():
    import _socket
    orig_select = _socket.select
    _socket.select = select.select

    try:
        fd = os.open(__file__, os.O_RDONLY)
        select.select([fd], [], [])
    finally:
        _socket.select = orig_select
        os.close(fd)

def test_select_interrupt():
    a = []

    class F:
        def fileno(self):
            os.kill(os.getpid(), signal.SIGINT)
            return
