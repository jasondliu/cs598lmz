import socket
# Test socket.if_indextoname()

def try_if_indextoname(indx):
    try:
        iname = socket.if_indextoname(indx)
    except ValueError:
        print("Couldn't get interface name for index %s." % indx)
    else:
        print("Interface name for index %s is %s." % (indx, iname))

try_if_indextoname(2)

try_if_indextoname(20)

try_if_indextoname(0)

try_if_indextoname(65534)

try_if_indextoname(65535)
