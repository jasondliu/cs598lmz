import socket
# Test socket.if_indextoname function.

# AF_PACKET family interface index to name mapping.
import socket
import sys

if sys.version_info < (3, 0):
    if 'linux' in sys.platform:
        # Linux AF_PACKET raw socket support.
        # We also require the presence of the file /proc/net/dev
        # to ensure we have a readable interface list.
        try:
            open('/proc/net/dev')
        except IOError:
            print('SKIP')
            sys.exit()
 
        s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
        s.bind(('lo', 0))
 
        # Find the index of loopback.
        for i in range(4):
            print(s.fileno(), socket.if_indextoname(i))
        # Should be on the range 0 to 3.
        s.close()
 
        # Find the name of the interface whose index is 1.
        print(socket.if_indextoname(1))
    else:

