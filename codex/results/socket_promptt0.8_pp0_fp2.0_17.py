import socket
# Test socket.if_indextoname()
socket.if_indextoname(1)
socket.if_indextoname(1, "foo")
socket.if_indextoname(1, "foo", "bar")
# Test socket.if_nametoindex
socket.if_nametoindex("lo")
socket.if_nametoindex("lo", "foo")
socket.if_nametoindex("lo", "foo", "bar")
# Test socket.getaddrinfo()
socket.getaddrinfo("lo", "http", proto=socket.IPPROTO_TCP)
socket.getaddrinfo("lo", "http", proto=socket.IPPROTO_TCP, flags=None)
socket.getaddrinfo("lo", "http", proto=socket.IPPROTO_TCP, flags=None,
                   family=socket.AF_UNSPEC)
socket.getaddrinfo("lo", "http", flags=None, family=socket.AF_UNSPEC)
socket.getaddrinfo("lo", "http", family=socket.AF_UNSPEC)
socket.getaddrinfo("lo", "http", family=
