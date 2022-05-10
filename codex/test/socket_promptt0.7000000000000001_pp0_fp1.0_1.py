import socket
# Test socket.if_indextoname() and socket.if_nameindex()
#
# if_indextoname() and if_nameindex() are only available on Linux
# platforms that support the SIOGIFNAME ioctl (introduced in 2.2.0).
#
import os
if not hasattr(socket, "if_indextoname"):
    print("SKIP")
    raise SystemExit

ifname = socket.if_indextoname(1)
print(ifname)

ifnames = socket.if_nameindex()
print(ifnames)

# Check that the table is not empty.
print(len(ifnames) > 0)
