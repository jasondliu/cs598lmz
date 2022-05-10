import socket
# Test socket.if_indextoname
print socket.if_indextoname(1)

print socket.if_indextoname(1, "eth0")

print socket.if_indextoname(1, "lo")

try:
    print socket.if_indextoname("foo")
except socket.error:
    print "socket.error: bad argument"
