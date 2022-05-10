import socket
# Test socket.if_indextoname()

def if_indextoname(ifindex):
    for i in range(ifindex):
        try:
            name = socket.if_indextoname(i)
        except:
            pass
        else:
            if name:
                print("%d: %s" % (i, name))

if_indextoname(32)
