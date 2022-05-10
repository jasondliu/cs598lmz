import socket
socket.if_indextoname(1)

# socket.if_nametoindex('lo')
socket.if_nametoindex('eth0')

# socket.gethostbyname('localhost')
socket.gethostbyname('www.google.com')

# socket.gethostbyname_ex('localhost')
socket.gethostbyname_ex('www.google.com')

# socket.gethostname()
# socket.getfqdn()

# socket.getaddrinfo('localhost', 80)
socket.getaddrinfo('www.google.com', 80)

# socket.getaddrinfo('localhost', 80, 0, 0, socket.IPPROTO_TCP)
socket.getaddrinfo('www.google.com', 80, 0, 0, socket.IPPROTO_TCP)

# socket.getaddrinfo('localhost', 80, 0, 0, socket.IPPROTO_UDP)
socket.getaddrinfo('www.google.com', 80, 0, 0, socket.IPPROTO_UDP)

# socket.getaddrinfo('localhost', 80, socket.AF_IN
