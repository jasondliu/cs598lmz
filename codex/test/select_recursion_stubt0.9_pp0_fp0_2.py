import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    assert select.select([], [f], [], 0) == ([], [f], [])

def test_select_closed_pipe():
    r, w = os.pipe()

    # add fd to the poller
    assert select.select([r], [], [], 0) == ([r], [], [])

    # close one of the fds and ensure that it does not raise EPIPE when polled
    os.close(w)

    # poller should silently ignore it
    assert select.select([r], [], [], 0) == ([r], [], [])
    # and return no data
    with os.fdopen(r) as f:
        assert f.read() == ''

def test_select_edge_trigger():
    r, w = os.pipe()

    os.write(w, b'x')
    os.write(w, b'y')

    select.select([r], [], [], 0)

    # the first byte was already read but the second byte is still there,
    # so select should return the file descriptor
   
