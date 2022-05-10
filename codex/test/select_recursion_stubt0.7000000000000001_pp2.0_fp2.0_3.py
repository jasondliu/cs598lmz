import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
        def read(self):
            return b""
        def write(self, data):
            a.append(data)

    f = F()

    select.select([f], [f], [f])


def test_select_read_never_returns():
    class F:
        def fileno(self):
            return 1
        def read(self):
            while True:
                pass

    f = F()

    start = time.time()
    select.select([f], [], [], 1)
    end = time.time()
    assert end - start <= 2


@pytest.mark.skipif(sys.platform == "win32", reason="Windows doesn't support non-blocking sockets")
def test_select_read_never_returns_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set to non-blocking
    s.setblocking(0)
