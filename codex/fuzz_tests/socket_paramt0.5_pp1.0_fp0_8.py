import socket
socket.if_indextoname(3)

# socket.if_nameindex()
# This method returns a list of tuples containing interface index and interface name.
socket.if_nameindex()

# socket.if_nametoindex(if_name)
# This method returns the interface index corresponding to the given interface name.
socket.if_nametoindex('lo')

# socket.getaddrinfo(host, port, family=0, type=0, proto=0, flags=0)
# This method returns a list of 5-tuples containing information about each matching address.
socket.getaddrinfo('www.google.com', 80)

# socket.getfqdn(name='')
# This method returns a fully qualified domain name for name.
socket.getfqdn('8.8.8.8')

# socket.gethostbyaddr(ip_address)
# This method returns a tuple containing hostname and a list of aliases for the given IP address.
socket.gethostbyaddr('8.8.8.8')

# socket.gethostbyname(hostname)
# This method returns the IP
