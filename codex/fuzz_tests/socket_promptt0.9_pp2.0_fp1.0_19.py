import socket
# Test socket.if_indextoname() on a tower with no wired adapter.
# Create a datagram socket
s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
# Bind to all interfaces
ifnetname = socket.if_indextoname(1)
print('Got ifnetname:', ifnetname)
if hasattr(socket, 'IPPROTO_IPV6'):
    proto = socket.IPPROTO_IPV6
else:
    proto = socket.IPPROTO_IP
s.setsockopt(proto, socket.IPV6_V6ONLY, 1)
print('Bind to', '[::]', 'on', ifnetname, 'with IPV6_V6ONLY', socket.IPV6_V6ONLY)
s.bind(('' '::', 0, 0, 0, 0, 0, 0, 0, 1))
print('Send from', '[::]', 'on', ifnetname, 'with IPV6_V6ONLY', socket.IPV6_V6ONLY)
s.sendto(b'6',
