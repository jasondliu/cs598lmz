import socket
socket.if_indextoname(3)

# socket.if_nameindex()
socket.if_nameindex()

# socket.if_nametoindex()
socket.if_nametoindex('en0')

# socket.getfqdn()
socket.getfqdn()

# socket.sethostname()
# socket.sethostname('jeff')

# socket.gethostname()
socket.gethostname()

# socket.gethostbyname()
socket.gethostbyname('google.com')

# socket.gethostbyname_ex()
socket.gethostbyname_ex('google.com')

# socket.gethostbyaddr()
socket.gethostbyaddr('8.8.8.8')

# socket.getaddrinfo()
socket.getaddrinfo('google.com', 80, 0, 0, socket.IPPROTO_TCP)

# socket.getnameinfo()
socket.getnameinfo(('8.8.8.8', 80), 0)

# socket.getdefaulttimeout()
socket.getdefaulttimeout()

# socket
