import socket
# Test socket.if_indextoname()
for interface in range(2**8):
    try:
        print socket.if_indextoname(interface)
    except Exception, e:
        pass
