import socket
# Test socket.if_indextoname() function

def test(family, address, expected):
    ifname = socket.if_indextoname(address)
    if ifname != expected:
        print("%s: %r != expected %r" % (address, ifname, expected))

test(socket.AF_INET, 0, "lo0")
test(socket.AF_INET, 1, "lo1")
test(socket.AF_INET, 2, "lo2")
test(socket.AF_INET, 3, "lo3")
test(socket.AF_INET, 4, "lo4")
test(socket.AF_INET, 5, "lo5")
test(socket.AF_INET, 6, "lo6")
test(socket.AF_INET, 7, "gif0")
test(socket.AF_INET, 8, "stf0")

test(socket.AF_INET6, 0, "lo0")
test(socket.AF_INET6, 1, "lo1")
