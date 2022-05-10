import socket
# Test socket.if_indextoname
def socket_if_indextoname_test():
    index = 2
    name = socket.if_indextoname(index)
