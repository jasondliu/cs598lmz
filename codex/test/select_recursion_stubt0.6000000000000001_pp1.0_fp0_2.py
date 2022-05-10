import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 42

        def read(self):
            a.append(1)

    select.select([F()], [], [], 0)
    assert a == [1]

def test_select_timeout():
    # Issue #9403: select() must not return before the timeout
    start = time.time()
    select.select([], [], [], 1)
    end = time.time()
    assert end - start >= 1

def test_select_keyboard_interrupt():
    # Issue #9403: select() must not swallow KeyboardInterrupt exceptions
    # occurring while it waits.
    class RaisingSocket(object):
        def __init__(self, *args):
            self.socket = socket.socket(*args)

        def fileno(self):
            return self.socket.fileno()

        def close(self):
            self.socket.close()

        def accept(self):
            raise KeyboardInterrupt

    listener = RaisingSocket(socket.AF_INET, socket.SOCK_STREAM)
