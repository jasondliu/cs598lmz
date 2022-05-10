import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 123

    s = select.select([], [F()], [], 0)
    l = a[:]
    test_select_mutated()
    assert s == ([], [], [])
    assert a == l

def test_select_error():
    with raises(TypeError):
        select.select(None, None, None)
    with raises(TypeError):
        select.select([], [], [], None)

def test_select_non_socket_fileno():
    class F:
        def fileno(self):
            return 123

    with raises(ValueError):
        select.select([F()], [F()], [F()])


def test_select_read_into():
    data = b"12345"
    s = socket.socket()
    s.bind(('localhost', 0))
    s.listen(1)
    s2, addr = s.accept()
    try:
        s2.send(data)
        a = bytearray(len(data))
        out = select.select([s2
