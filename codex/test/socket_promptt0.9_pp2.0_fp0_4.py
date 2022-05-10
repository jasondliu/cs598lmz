import socket
# Test socket.if_indextoname() on (all) interfaces.
#
# This ensures that the netifaces code provides the same names
# as the underlying system. In many cases these names are defined
# by the unpacking system.
#
# If a machine has no network interfaces, this test is skipped.
if __name__ == '__main__':
    for i in range(256):
        try:
            socket.if_indextoname(i)
        except IOError as e:
            if e.errno == errno.EINVAL:
                break
            if e.errno == errno.EADDRNOTAVAIL:
                continue
            raise
        except Exception as e:
            raise
        else:
            print(socket.if_indextoname(i))
