import socket
# Test socket.if_indextoname()
print socket.if_indextoname(1)
print socket.if_indextoname(2)
print socket.if_indextoname(3)
print socket.if_indextoname(4)
print socket.if_indextoname(5)

print "\nPrinting all interfaces"
print socket.if_nameindex()

print "\nPrinting all interfaces by family"
print socket.if_nameindex(socket.AF_INET)
print socket.if_nameindex(socket.AF_INET6)
