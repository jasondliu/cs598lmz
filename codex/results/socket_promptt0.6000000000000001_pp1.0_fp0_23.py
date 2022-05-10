import socket
# Test socket.if_indextoname()
for i in range(0, 16):
    try:
        ifname = socket.if_indextoname(i)
        print(ifname)
    except OSError as e:
        print("%d: %s" % (e.errno, e.strerror))
    except:
        print("Unexpected error:", sys.exc_info()[0])
