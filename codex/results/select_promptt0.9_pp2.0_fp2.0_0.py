import select
# Test select.select, select.poll and select.epoll (on Linux).
# poll() is not the same across platforms: the 'poll' module
# tries to emulate it using select on other platforms.
# epoll() is Linux-specific but works like select().epoll()
# select() supports polling on sockets only.

def test_select(s_and_a, poll, epoll):
    # create a bunch of clients connected to the same server
    N = 5
    clients = [socket.socket(socket.AF_INET, socket.SOCK_STREAM)
               for i in range(N)]
    for c in clients:
        c.connect(s_and_a)
        # write the data in N chunks and read it back
        for i in range(N):
            c.send(b'x')
            # the server echoes in chunks if the chunk size is > 1
            assert c.recv(1) == b'x'
        c.close()
    # reveal that all sockets were dequeued and closed
    clients = [c for c in clients if c.fileno() != -
