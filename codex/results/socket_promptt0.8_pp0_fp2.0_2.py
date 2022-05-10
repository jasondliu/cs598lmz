import socket
# Test socket.if_indextoname()
if socket.has_ipv6:
    try:
        assert socket.if_indextoname(1)
    except ValueError:
        pass # Could not find interface index 1
    assert socket.if_indextoname(socket.if_nametoindex('lo')) == 'lo'

# Test socket.getservbyport()
try:
    assert socket.getservbyport(22)
except socket.error:
    pass # Could not find service for port 22

# Test socket.getaddrinfo()
try:
    assert socket.getaddrinfo('www.python.org', 80)
except socket.gaierror:
    pass # Could not find address: www.python.org

# Test socket.getnameinfo()
info = socket.getaddrinfo('www.python.org', 80, 0, 0, socket.IPPROTO_TCP)
assert info[0][4][:2] == ('216.34.181.97', 80)
assert socket.getnameinfo(('216.34.181.97', 80), 0)

# Test
