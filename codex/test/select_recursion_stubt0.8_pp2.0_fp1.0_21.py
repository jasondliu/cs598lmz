import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    def f( F ):
        a.append( F )

    b = select.select( [f(1), f(2), f(3)], (), (), 0 )
    assert a == b[0], "select mutated its sequence argument"

def recv_some(conn):
    flags = fcntl.fcntl(conn, fcntl.F_GETFL, 0)
    fcntl.fcntl(conn, fcntl.F_SETFL, flags | os.O_NONBLOCK)
    try:
        return conn.recv(1024)
    except socket.error:
        pass

def test_select_error():
    """
    Tests that the select function checks for errors in the FDs given to it, even
    if none of the FDs is ready for a given operation.
    """
    serv = socket.socket()

    # Depending on the system, a connection to an unreachable IP will either
    # give an error right away or wait a while.  Since we're going to do lots
    # of
