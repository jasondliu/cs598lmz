import socket
# Test socket.if_indextoname/socket.if_nameindex

import socket, sys

if sys.platform[:3] == "win":
    print("Not applicable on Windows")
    sys.exit(0)

# On some platforms the underlying calls to the kernel require root permissions
if sys.platform[:5] == 'linux':
    try:
        socket.if_nameindex()
    except OSError as err:
        import errno
        if err.errno != errno.EPERM:
            raise
        print("Skipping test due to insufficient permissions")
        sys.exit(0)

# Try to find a valid interface index.
try:
    idx = socket.if_nameindex()[0][0]
except:
    print("No valid interface index found, skipping test")
    sys.exit(0)

name = socket.if_indextoname(idx)
print("Name for index %d is %s" % (idx, name))
if socket.if_indextoname(idx) != name:
    print("Name conversion failed")

