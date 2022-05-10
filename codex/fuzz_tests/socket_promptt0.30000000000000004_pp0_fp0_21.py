import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    if ifname is None:
        print("if_indextoname(1) returned None")
        return
    print("if_indextoname(1) returned", ifname)
    if ifname != 'lo':
        print("if_indextoname(1) returned", ifname, "instead of 'lo'")
        return
    print("if_indextoname(1) returned 'lo'")

test_if_indextoname()
