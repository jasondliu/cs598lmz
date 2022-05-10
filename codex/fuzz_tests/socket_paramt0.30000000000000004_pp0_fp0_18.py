import socket
socket.if_indextoname(3)

# socket.if_nameindex()
# returns a list of tuples containing interface name and index
socket.if_nameindex()

# socket.if_nametoindex(if_name)
# returns the index of the interface
socket.if_nametoindex('lo')

# socket.gethostbyname(hostname)
# returns the IP address of the hostname
socket.gethostbyname('www.google.com')

# socket.gethostbyname_ex(hostname)
# returns the IP address of the hostname and the list of aliases
socket.gethostbyname_ex('www.google.com')

# socket.gethostbyaddr(ip_address)
# returns the hostname and the list of aliases for the IP address
socket.gethostbyaddr('216.58.216.164')

# socket.gethostname()
# returns the hostname of the machine
socket.gethostname()

# socket.getfqdn()
# returns the fully qualified domain name of the machine
socket.getfqdn()

# socket.get
