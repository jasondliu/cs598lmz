import socket
# Test socket.if_indextoname
for i in range(0, 10):
    try:
        socket.if_indextoname(i)
    except Exception, e:
        pass
    assert socket.if_indextoname(i) is None
# Test socket.if_nameindex
nif = socket.if_nameindex()
if len(nif) > 0:
    interface = nif[0]
    assert interface[0] != 0
    assert interface[1] != 0
# Test socket.if_nametoindex
assert socket.if_nametoindex('lo') != 0
# Test socket.gethostbyname
assert socket.gethostbyname('localhost') == '127.0.0.1'
# Test socket.getservbyname
assert socket.getservbyname('http') == 80
# Test socket.getaddrinfo
infos = socket.getaddrinfo('localhost', 80, 0, 0, socket.IPPROTO_TCP)
assert len(infos) > 0
info = infos[0]
assert len(info) == 5
assert info[0] == 2

