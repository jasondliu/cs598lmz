import socket
# Test socket.if_indextoname()

import socket

def test(family, ifindex):
    print(socket.if_indextoname(ifindex, family))

def test_all():
    test(socket.AF_INET, 2)
    test(socket.AF_INET6, 2)

test_all()
