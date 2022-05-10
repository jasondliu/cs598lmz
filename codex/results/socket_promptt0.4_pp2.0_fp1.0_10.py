import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    if ifname:
        print("index 1 is", ifname)
    else:
        print("index 1 is not found")

test_if_indextoname()
