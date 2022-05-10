import socket
# Test socket.if_indextoname()
def getInterface(ifindex):
    """Return the name of an interface, given the index
The index is converted to an integer, if necessary"""
    return socket.if_indextoname(ifindex)

