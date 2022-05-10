import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    a.append(F())
    try:
        select.select([], [], a)
    except ValueError:
        pass
    else:
        raise SystemError

def test_select_closed_pipe():
    # Issue #8313: select() should not raise an error when passed a closed pipe
    r, w = os.pipe()
    os.close(r)
    os.close(w)
    select.select([r], [], [], 0)

def test_select_closed_file():
    # Issue #8313: select() should not raise an error when passed a closed file
    f = open(test.support.TESTFN, 'wb')
    f.close()
    select.select([f], [], [], 0)

def test_select_closed_socket():
    # Issue #8313: select() should not raise an error when passed a closed socket
    s = socket.socket()
    s.close()
    select.select([s], [], [], 0)

