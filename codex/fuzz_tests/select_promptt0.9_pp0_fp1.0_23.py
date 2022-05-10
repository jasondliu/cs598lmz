import select
# Test select.select() makes cross-platform comparisons to poll.poll() results more straightforward
s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
s.bind(('', 8888))
s.setblocking(0)
s.connect(('::1', 9999))
r, w, e = select.select([], [s], [], 0)
print(r, w, e)   # [] [<socket.socket fd=6, family=AddressFamily.AF_INET6, type=SocketKind.SOCK_DGRAM, proto=0>] []

s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
s.bind(('', 8888))
s.setblocking(0)
s.connect(('::1', 9999))
r, w, e = select.select([], [s], [], 0)
print(r, w, e)   # [] [<socket.socket fd=6, family=AddressFamily.AF_INET6, type=SocketKind.SOCK_DGRAM
