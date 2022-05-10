import socket
# Test socket.if_indextoname ---------------------------------------------------------------------------------------------------------

print("\nTest socket.if_indextoname--------------------------------------------------------------------------------------------")
print("socket.if_indextoname(1): " + socket.if_indextoname(1))

# Test socket.if_nameindex ----------------------------------------------------------------------------------------------------------

print("\nTest socket.if_nameindex------------------------------------------------------------------------------------------------")
print("socket.if_nameindex(): " + str(socket.if_nameindex()))

# Test socket.if_nametoindex --------------------------------------------------------------------------------------------------------

print("\nTest socket.if_nametoindex------------------------------------------------------------------------------------------------")
print("socket.if_nametoindex('eth0'): " + str(socket.if_nametoindex("eth0")))

# Test socket.getaddrinfo -----------------------------------------------------------------------------------------------------------

print("\nTest socket.getaddrinfo---------------------------------------------------------------------------------------------------")
print("socket.getaddrinfo('www.microsoft.com', 'http'): " + str(socket.getaddrinfo("www.microsoft.com", "http")))
