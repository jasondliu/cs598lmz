import socket
socket.if_indextoname(5)

#if_nametoindex
import socket
socket.if_nametoindex('lo')

#if_nameindex
import socket
socket.if_nameindex()

#if_freenameindex
import socket
socket.if_freenameindex(2)

#gethostbyname
import socket
socket.gethostbyname('www.google.com')

#gethostbyname_ex
import socket
socket.gethostbyname_ex('www.google.com')

#gethostbyaddr
import socket
socket.gethostbyaddr('216.58.213.110')

#gethostname
import socket
socket.gethostname()

#getfqdn
import socket
socket.getfqdn('216.58.213.110')

#getnameinfo
import socket
socket.getnameinfo(('216.58.213.110',80),0)

#getaddrinfo
import socket
socket.getaddrinfo('www.google.com',80)

#getdefaulttimeout
import socket
socket.getdefaulttimeout()
