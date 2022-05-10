import socket
# Test socket.if_indextoname()

import socket, os, sys

# Obtain interface name from the command line
ifname = sys.argv[1]

# Obtain the index for the interface name
ifindex = socket.if_nametoindex(ifname)

# Retrieve the interface name from the index
print "Index %d = interface %s" % (ifindex, socket.if_indextoname(ifindex))
