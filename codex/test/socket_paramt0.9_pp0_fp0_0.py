import socket
socket.if_indextoname(0)
# get the address
"""
 you can use if_indextoname to obtain the name of the interface, and then use gethostbyname to
 obtain its IP address
 """
print(socket.gethostbyname('wlan0'))
"""
Although the OS knows about an IP address for an interface, it does not always use it. For instance,
 when IP aliasing is used and an interface has more than one IP address, calling socket.gethostbyname
 with the name of the interface will return only the first IP address. In this case, you must call 
 getsockaddrbyifname to get a tuple of all addresses available to a given interface
 """
print(socket.getsockaddrbyifname('eth0'))

