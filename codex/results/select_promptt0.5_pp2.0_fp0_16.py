import select
# Test select.select()

# Create a pair of connected sockets
s1, s2 = socket.socketpair()

for i in range(5):
    rlist, wlist, xlist = select.select([s1], [s2], [s1, s2], 1.0)
    print(i, rlist, wlist, xlist)
    # We expect that s1 is always readable, s2 is always writable,
    # and that exceptions only occur on the last iteration
    # when the connection is closed.
    if s1 in rlist:
        data = s1.recv(1024)
        print('Received', repr(data))
    if s2 in wlist:
        s2.send(b'This is a test')

# Clean up
s1.close()
s2.close()
