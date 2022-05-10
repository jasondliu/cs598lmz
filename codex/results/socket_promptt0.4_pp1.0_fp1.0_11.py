import socket
# Test socket.if_indextoname()

def test(family, addr):
    try:
        ifname = socket.if_indextoname(addr)
        print('if_indextoname(%d): %s' % (addr, ifname))
        ifaddr = socket.if_nameindex()
        print('if_nameindex(): %r' % ifaddr)
    except socket.error as msg:
        print('if_indextoname(%d): %s' % (addr, msg))

test(socket.AF_INET, 0)
test(socket.AF_INET, 1)
test(socket.AF_INET, 2)
test(socket.AF_INET, 3)
