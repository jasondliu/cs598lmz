import socket
socket.if_indextoname(3)

# gethostbyname
socket.gethostbyname('www.python.org')

# gethostbyname_ex
socket.gethostbyname_ex('www.python.org')

# gethostbyaddr
socket.gethostbyaddr('93.184.216.34')

# getnameinfo
socket.getnameinfo(('93.184.216.34', 80), 0)

# getfqdn
socket.getfqdn('93.184.216.34')

# getaddrinfo
socket.getaddrinfo('www.python.org', 'http')

# getdefaulttimeout
socket.getdefaulttimeout()

# setdefaulttimeout
socket.setdefaulttimeout(10)

# create_connection
socket.create_connection(('www.python.org', 80))

# SocketServer
import SocketServer

class EchoRequestHandler(SocketServer.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        self.logger = server.logger
