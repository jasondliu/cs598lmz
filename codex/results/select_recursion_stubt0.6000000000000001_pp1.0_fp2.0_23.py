import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], [], [], 0) # Trigger the mutation

    # Check that the select loop is still working
    s = socket.socket()
    s.bind(('127.0.0.1', 0))
    s.listen(5)
    w = socket.socket()
    w.connect(s.getsockname())

    select.select([s], [], [], 0) # Should not crash

def test_select_closed_socket():
    s = socket.socket()
    s.bind(('127.0.0.1', 0))
    s.listen(5)

    r = socket.socket()
    r.connect(s.getsockname())

    select.select([s], [], [], 0) # Should not crash

    r.close()
    s.close()

    select.select([s], [], [], 0) # Should not crash

def test_select_closed_pipe():
    r, w = os.pipe()

    select.select([r], [], [], 0) #
