import select
# Test select.select timeout feature
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind(('127.0.0.1', 0))

# UDP test -- select() should always succeed
#
# The timeout test relies upon the socket always being ready, which
# is not the case for UDP.  A long-enough timeout can solve this, but
# we're not doing that.
res = select.select([], [udp], [], 0.0)
print res

# Unix domain socket test
s1, s2 = socket.socketpair()
s1.setblocking(0)
s2.setblocking(0)

# Send data to s2 from s1
s1.send('x')

# Do select() with a timeout.  It should always succeed, because
# there is data waiting on the socket.
res = select.select([s2], [], [], 1.0)
print res
