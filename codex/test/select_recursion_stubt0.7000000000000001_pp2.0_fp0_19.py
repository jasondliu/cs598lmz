import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    s = select.select([f], [], [])
    assert not s, 'select() returned a non-empty list'

def test_select_bad_fd():
    fd = -1
    while True:
        try:
            fd = os.dup(fd)
        except OSError as e:
            if e.errno == errno.EMFILE:
                break
    try:
        assert select.select([fd], [], []) == ([], [], [])
    finally:
        os.close(fd)

def test_select_exc_in_poll():
    class BadIO:
        def fileno(self):
            return 123
        def poll(self):
            raise IOError
        def __repr__(self):
            return '<BadIO>'
    def poll(self, timeout=None):
        try:
            return select.poll.poll(self, timeout)
        except IOError:
            return []
    select.poll.poll = poll

