import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    if ifname is None:
        print("No interface with index 1")
    else:
        print("Interface with index 1 is", ifname)

test_if_indextoname()
