import socket
socket.if_indextoname('3')

# getnameinfo
socket.getnameinfo(('127.0.0.1', 8080), 0)

# gethostbyname_ex
socket.gethostbyname_ex('www.python.org')

# gethostbyaddr
socket.gethostbyaddr('127.0.0.1')

# gethostname
socket.gethostname()

# getservbyport
socket.getservbyport(80)

# socket.getfqdn
socket.getfqdn()
