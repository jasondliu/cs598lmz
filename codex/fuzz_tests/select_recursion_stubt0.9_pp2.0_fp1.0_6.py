import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    s = select.select([F()], [], [], 0)
    assert a


def test_select_rlist():
    a = []

    class F:
        def fileno(self):
            a.append(1)
        def recv(self, bufsize, flags=0):
            a.append(2)
        def send(self, b):
            a.append(3)
        def sendto(self, b, addr):
            a.append(4)
        def recvfrom(self, bufsize, flags=0):
            a.append(5)
        def recvfrom_into(self, buffer, nbytes=0, flags=0):
            a.append(6)
        def sendall(self, b, flags=0):
            a.append(7)
        def connect(self, address):
            a.append(8)
        def accept(self):
            a.append(9)

    fd = F()
    s = select.select([fd, fd], [],
