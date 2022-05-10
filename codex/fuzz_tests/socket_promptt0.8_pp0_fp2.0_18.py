import socket
# Test socket.if_indextoname()

import sys
import socket
import os

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: if_indextoname.py index"
        sys.exit(2)
    interface_name = socket.if_indextoname(int(sys.argv[1]))
    print interface_name
    if os.name == 'nt':
        # XXX On Windows, we can't easily look up the interface name
        # given its index.
        print 'skipping lookup of index'
    else:
        interface_index = socket.if_nametoindex(interface_name)
        print interface_index
