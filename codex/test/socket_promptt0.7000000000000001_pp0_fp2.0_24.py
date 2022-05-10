import socket
# Test socket.if_indextoname
for i in range(0, 128):
    try:
        iface = socket.if_indextoname(i)
        if iface == None:
            continue
        idx = socket.if_nametoindex(iface)
        if idx != i:
            print("Test fail:", iface, idx)
    except Exception as e:
        print("Test fail:", i, e)
