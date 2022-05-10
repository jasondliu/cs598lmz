import socket
# Test socket.if_indextoname()
import errno

def test():
    try:
        socket.if_indextoname(0)
    except socket.error as e:
        if e.args[0] != errno.ENXIO:
            raise
    else:
        raise

if __name__ == '__main__':
    test()
