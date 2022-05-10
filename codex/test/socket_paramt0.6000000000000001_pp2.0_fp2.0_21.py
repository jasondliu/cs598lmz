import socket
socket.if_indextoname(1)

# If you want to know the interface name of the IP address, you can use the function gethostbyaddr()
socket.gethostbyaddr('192.168.0.1')

# If you want to know the IP address of the interface name, you can use the function gethostbyname()
socket.gethostbyname('eth0')

# If you want to know the network interface name, you can use the function gethostname()
socket.gethostname()

# If you want to know the IP address of the network interface name, you can use the function gethostbyname()
socket.gethostbyname('lo')

# If you want to know all the IP addresses of the interface name, you can use the function gethostbyname_ex()
socket.gethostbyname_ex('lo')

# If you want to know the network interface name, you can use the function gethostname()
socket.gethostname()

# If you want to know the IP address of the network interface name, you can use the function gethostbyname()
socket.gethostbyname('eth0')
