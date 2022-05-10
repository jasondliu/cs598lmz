import socket
# Test socket.if_indextoname() (lp:937362)

if __name__ == '__main__':
    import support
    import os
    import sys
    try:
        socket.if_indextoname(if_nametoindex('lo'))
    except OSError:
        raise support.TestError('failed to find if_nametoindex')

    try:
        socket.if_nametoindex('10000000')
    except ValueError:
        pass
    else:
        raise support.TestError('failed to reject invalid if_nametoindex')
