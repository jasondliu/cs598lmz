import socket
socket.if_indextoname(2)

#socket.AF_INET

# socket.getfqdn(some_ipv6_address)
socket.gethostbyname('www.python.org')
#socket.gethostname()
#socket.gethostbyname_ex('www.python.org')
#socket.gethostbyaddr('140.211.11.104')

#socket.getaddrinfo('www.python.org', 'www')
#socket.getaddrinfo('www.python.org', 'ssh')


socket.getdefaulttimeout()
#socket.setdefaulttimeout(10) # you may need superviser privilege



# create a raw socket
sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname('icmp'))
#sock.setsockopt(socket.SOL_SOCKET, SO_BINDTODEVICE, bytes(interface,'utf-8'))
sock.bind(('192.168.1.1', 0))
sock.connect(('www.python.org', 80))
