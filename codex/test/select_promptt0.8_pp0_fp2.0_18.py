import select
# Test select.select timeout feature
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind(('127.0.0.1', 0))

# UDP test -- select() should always succeed
#
# The timeout test relies upon the socket always being ready, which
# is not the case for UDP.  A long-enough timeout can solve this, but
# we're not doing that.
