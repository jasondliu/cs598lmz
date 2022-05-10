import select
# Test select.select()

# Create a pair of connected sockets

def test_select():
    if not hasattr(select, "poll"):
        print("poll not defined -- skipping test_select")
        return

    (s1, s2) = socket.socketpair()
    s1.setblocking(0)
    s2.setblocking(0)

    # Create a poll object
    p = select.poll()

    # Register s1 and s2 for read events
    p.register(s1, select.POLLIN)
    p.register(s2, select.POLLIN)

    # Send some data from s1 to s2
    s1.send(b"x" * 100000)

    # Poll for read events
    for fd, event in p.poll(1000):
        if fd == s1.fileno():
            data = s1.recv(1024)
            if not data:
                print("s1 closed")
                break
        elif fd == s2.fileno():
            data = s2.recv(1024)
            if
