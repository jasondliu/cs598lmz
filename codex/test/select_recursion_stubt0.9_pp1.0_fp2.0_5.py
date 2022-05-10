import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 5

    a.append(F())
    s = select.select([], a, [])
    a.pop()

def test_big_poll():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    s.listen()
    s.setblocking(0)
    # On Linux, you need to consume the first connection
    # attempt here before sending a lot of SYN packets.
    # Otherwise the kernel silently drops SYN packets
    # instead of putting them in the backlog.
    s.accept()
    # Connect to port, but don't complete the 3-way handshake.
    # Send enough of these requests such that the kernel
    # will end up dropping the connection requests.
    connections = [socket.socket() for i in xrange(10000)]
    for c in connections:
        c.connect(("127.0.0.1", s.getsockname()[1]))
    r, w, e = select.select([], connections, [], 10)
    r, w, e = select.select
