import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    if ifname:
        print("Interface name:", ifname)
    else:
        print("Interface name not found")

test_if_indextoname()
