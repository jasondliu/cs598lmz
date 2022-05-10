import socket
socket.if_indextoname(3)
socket.if_nametoindex('wlo1')
socket.gethostbyname('www.python.org')
socket.gethostbyname_ex('www.python.org')
socket.gethostbyaddr('216.58.208.238')

# Socket Options
socket.getdefaulttimeout()
socket.setdefaulttimeout(1)
socket.getdefaulttimeout()
socket.setdefaulttimeout(None)
socket.getdefaulttimeout()

# TCP Socket
#   AF_INET: IPv4
#   SOCK_STREAM: TCP
#   SOCK_DGRAM: UDP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 0))
s.getsockname()

# TCP Server
#   listen()
#   accept()
#   recv()
#   sendall()
#   send()
#   close()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 1234))
s.listen(
