import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return F.fileno(self)
        def read(self):
            return b'foo'

    assert select.select([F()], [], []) == ([], [], [])
    raises(ZeroDivisionError, a.pop)

def test_select_keyboard_interrupt():
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #
    try:
        raises(select.error, select.select, [s], [s], [s], 1)
    except KeyboardInterrupt:
        e = sys.exc_info()[1]
        assert e.args[0] == errno.EINTR
