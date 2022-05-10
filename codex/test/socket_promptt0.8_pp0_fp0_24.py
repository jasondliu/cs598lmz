import socket
# Test socket.if_indextoname
def test_socket_if_indextoname():
    assert 'lo'==socket.if_indextoname(1)

# Test socket.sendmsg
def test_socket_sendmsg():
    ipv6only = socket.IPPROTO_IPV6
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, ipv6only)
    data = bytes('hello', 'utf-8')
    addr = ('::', 8080)
    n = sock.sendto(data, 0, addr)
    assert n == 5

# Test socket.recvmsg
def test_socket_recvmsg():
    ipv6only = socket.IPPROTO_IPV6
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
