import socket
# Test socket.if_indextoname
assert socket.if_indextoname(1) == "lo"
# Test socket.if_nametoindex
assert socket.if_nametoindex("lo") == 1
# Test socket.getnameinfo
assert socket.getnameinfo((b"127.0.0.1", 80), socket.NI_NAMEREQD) == ("localhost", 80)
# Test socket.getfqdn
assert socket.getfqdn("127.0.0.1") == "localhost"
# Test socket.getaddrinfo
assert socket.getaddrinfo("localhost", None) == [
    (2, 1, 6, "", ("127.0.0.1", 0)),
    (10, 1, 6, "", ("127.0.0.1", 0)),
    (2, 2, 17, "", ("127.0.0.1", 0)),
    (10, 2, 17, "", ("127.0.0.1", 0)),
]

import ipaddress
# Test ipaddress.ip_address
