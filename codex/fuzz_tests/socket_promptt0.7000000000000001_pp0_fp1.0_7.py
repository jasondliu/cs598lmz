import socket
# Test socket.if_indextoname()
# Adapted from Lib/test/test_socket.py

import socket

if socket.has_ipv6:
    def test(indx):
        name = socket.if_indextoname(indx)
        if name is not None:
            if socket.if_nameindex().index(name) == indx:
                print("OK: index %d name %s" % (indx, name))
            else:
                print("FAIL: index %d name %s" % (indx, name))
        else:
            print("FAIL: index %d name returned None" % (indx,))
    #
    for indx in range(0, 1024):
        test(indx)
