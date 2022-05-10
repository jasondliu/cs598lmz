import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], a, a)

def test_socket_mutated():
    a = []

    class F:
        def fileno(self):
            test_socket_mutated()
            return 0

    socket.fromfd(F().fileno(), socket.AF_INET, socket.SOCK_STREAM)

def test_socket_sendfile_mutated():
    class F:
        def fileno(self):
            test_socket_sendfile_mutated()
            return 0

    socket.socket(socket.AF_INET, socket.SOCK_STREAM).sendfile(F(), 0, 0)

def test_socket_recvfrom_mutated():
    class F:
        def fileno(self):
            test_socket_recvfrom_mutated()
            return 0

    socket.socket(socket.AF_INET, socket.SOCK_STREAM).recvfrom(F(), 0)

def test_socket_recvfrom_into_mutated():
    class F:
        def fil
