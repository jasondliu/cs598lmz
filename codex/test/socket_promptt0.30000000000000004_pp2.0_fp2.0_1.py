import socket
# Test socket.if_indextoname()

def test_if_indextoname(ifname):
    print("if_indextoname(%s) = %s" % (ifname, socket.if_indextoname(ifname)))

test_if_indextoname(1)
test_if_indextoname(2)
test_if_indextoname(3)
test_if_indextoname(4)
test_if_indextoname(5)
test_if_indextoname(6)
test_if_indextoname(7)
test_if_indextoname(8)
test_if_indextoname(9)
test_if_indextoname(10)
test_if_indextoname(11)
test_if_indextoname(12)
test_if_indextoname(13)
test_if_indextoname(14)
test_if_indextoname(15)
test_if_indextoname(16)
