import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    a.append(F())
    ret = select(a, a, a, 1000)


def test_socket_leak_with_close():
    import socket
    s = socket.socket()
    s.connect(("www.python.org", 80))
    s.close()
#    print("DEAD:", s._closed)
    assert s._closed


def test_socket_leak_with_pop():
    import socket
    a = []
    for i in range(100):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setblocking(0)
        try:
            s.connect(("www.python.org", 80))
        except ConnectionRefusedError:
            pass
        a.append(s)
    while a:
        a.pop()


def test_socket_leak_with_close_in_except():
    import socket
    s = socket.socket()
    try:
        s.connect(("www.python.orgxyz", 80))
    except
