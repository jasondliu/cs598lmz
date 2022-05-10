import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    if ifname:
        print("Interface 1 is %s" % ifname)
    else:
        print("Interface 1 not found")

test_if_indextoname()
