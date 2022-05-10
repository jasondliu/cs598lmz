import socket
# Test socket.if_indextoname()

def test_if_indextoname(if_indextoname):
    itn = if_indextoname[0]
    if_indextoname = if_indextoname[1]
    ifacenames = socket.if_nameindex()
    for iface in ifacenames:
        name = if_indextoname(iface[0])
        if name not in itn:
            print("Failed to find name %s" % name)
            print("Names are:", itn)
            return False
    return True
