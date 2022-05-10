import socket
# Test socket.if_indextoname()

# Socket should be created using socket.AF_PACKET and
# socket.SOCK_RAW to be able to use ioctl calls.
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)

# Get the list of interfaces
if_nametoindex = socket.if_nametoindex("eth0")

print("Index for interface eth0 is: %d" % if_nametoindex)

if_indextoname = socket.if_indextoname(if_nametoindex)

print("Interface name for index %d is: %s" % (if_nametoindex, if_indextoname))

# Close the socket
s.close()
