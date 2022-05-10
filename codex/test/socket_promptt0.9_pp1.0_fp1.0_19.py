import socket
# Test socket.if_indextoname()
#
# The socket should exist in the test environment
IFNAME0 = 'eth0'

def interfacename():
    try:
        return socket.if_indextoname(socket.if_nametoindex(IFNAME0))
    except OSError:
        pass

def if_indextoname():
    try:
        index = socket.if_nametoindex(IFNAME0)
    except OSError:
        pass
    try:
        return [socket.if_indextoname(index)]
    except OSError:
        pass
    try:
        if addr_only:
            return socket.if_indextoname(index, only_if_address)
        else:
            return socket.if_indextoname(index, has_if_address)
    except OSError:
        pass
