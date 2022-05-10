import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    # Set the fd to be 3
    f = F()
    a.append(3)

    select.select([f], [f], [f], None)
    del f

    f = F()
    a.append(3)
    select.select([f], [f], [f], None)
    del f

# Is a pipe on windows?
if sys.platform=='win32':
    def test_select():
        rfds, wfds, xfds = select.select([], [], [], 0.001)
        assert rfds == []
        assert wfds == []
        assert xfds == []

# TODO The following tests would be useful to have on windows.
# How to run with a socket on win32?
if False:
    def test_select_read():
        rfds, wfds, xfds = select.select([self.v[0]], [], [], 0.001)
        assert rfds == []
        assert wfds == []
        assert
