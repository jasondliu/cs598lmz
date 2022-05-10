import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 97

    f = F()
    try:
        select.select([f], [], [], 0)
    except select.error, e:
        pass
    else:
        raise AssertionError, 'did not get exception!'
    try:
        del a[:]
    finally:
        del a

def test_issue8049():
    """
    Checks that the WSAGetLastError call present in socketmodule.c for
    Windows handles the errno ENOTCONN properly.  This was broken when
    issue7368 was fixed, causing the case where a send() method
    following a sendall() method failed with a particular error to
    return ENOTCONN instead of the real error.
    """
    import socket
    s = socket.socket()

    # First, try to simulate what happens when a blocking socket isn't
    # connected.  This is the "standard" case.
    try:
        s.setblocking(1)
        s.send("foo")
    except socket.error as e:
        assert e.args[0] not in (err
