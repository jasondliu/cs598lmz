import select
# Test select.select()

# Create a pair of connected sockets

if os.name == 'posix':
    # On POSIX, the best timer is select()
    from select import select
    def timer_func():
        return select([], [], [], 0.1)
else:
    # On Windows, the best timer is time.clock()
    from time import clock
    def timer_func():
        start = clock()
        while clock() == start:
            pass

def test_select():
    import socket
    s1, s2 = socket.socketpair()
    for i in range(100):
        result = select.select([s1], [s1], [s1], 0.1)
        assert result == ([], [], []), result
        s2.send(b'x')
        assert s1.recv(100) == b'x'
        timer_func()
    s1.close()
    s2.close()

def test_select_timeout():
    import socket
    s1, s2 = socket.socketpair()
    for i in range
