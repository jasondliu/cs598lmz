import socket
# Test socket.if_indextoname() on a Linux system
# https://docs.python.org/2/library/socket.html#socket.if_indextoname
# https://github.com/python/cpython/blob/2.7/Modules/socketmodule.c#L2168
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for i in range(256):
    try:
        print('{:3d} {:>10}'.format(i, socket.if_indextoname(i)))
    except:
        pass

# vim: set ft=python ai ts=4 sw=4 sts=4 et:
