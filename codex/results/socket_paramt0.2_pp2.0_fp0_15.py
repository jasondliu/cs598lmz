import socket
socket.if_indextoname(3)

# 'en0'

# socket.if_nameindex()
# Returns a list of tuples containing interface indexes and names.

# socket.if_nametoindex(name)
# Returns the interface index of the given interface name.

# socket.gethostbyname(hostname)
# Returns the IP address of the given hostname.

# socket.gethostbyname_ex(hostname)
# Returns a tuple containing the hostname, a list of aliases, and a list of IP addresses.

# socket.gethostname()
# Returns the hostname of the current machine.

# socket.gethostbyaddr(ip_address)
# Returns a tuple containing the hostname, a list of aliases, and a list of IP addresses.

# socket.getfqdn(hostname)
# Returns the fully qualified domain name of the given hostname.

# socket.getaddrinfo(host, port, family=0, type=0, proto=0, flags=0)
# Returns a list of tuples containing information about each address.

# socket.getnameinfo(
