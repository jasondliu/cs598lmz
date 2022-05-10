import socket
# Test socket.if_indextoname

def test(family, ip):
    ifname = socket.if_indextoname(ip)
    if ifname is None:
        print('%s: %s' % (ip, '<not found>'))
    else:
        print('%s: %s' % (ip, ifname))

test(socket.AF_INET, 1)
test(socket.AF_INET, 2)
test(socket.AF_INET, 3)
test(socket.AF_INET, 4)
test(socket.AF_INET, 5)
test(socket.AF_INET, 6)
test(socket.AF_INET, 7)
test(socket.AF_INET, 8)
test(socket.AF_INET, 9)
test(socket.AF_INET, 10)
test(socket.AF_INET, 11)
test(socket.AF_INET, 12)
test(socket.AF_INET, 13)
test(socket.AF_INET, 14)
