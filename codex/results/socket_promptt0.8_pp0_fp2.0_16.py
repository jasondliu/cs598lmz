import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(3))
print(socket.if_indextoname(4))
print(socket.if_indextoname(5))
print(socket.if_indextoname(2))
print(socket.if_indextoname(1))
print(socket.if_indextoname(0))

# Print all the interfaces that are listed
import netifaces
print(netifaces.interfaces())


# Get the details of the interfaces

# The names of the interfaces
print(netifaces.interfaces())

# Get the addresses of the interfaces
print(netifaces.ifaddresses('en0'))


# Get the IPv4 address of the interface
print(netifaces.ifaddresses('en0')[netifaces.AF_INET])
print(netifaces.ifaddresses('en0')[netifaces.AF_INET][0]['addr'])
print(netifaces.ifaddresses('en0')[netifaces.AF_INET][0]['netmask
