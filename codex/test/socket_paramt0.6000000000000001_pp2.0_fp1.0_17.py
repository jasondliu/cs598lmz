import socket
socket.if_indextoname(3)
socket.if_nameindex()
socket.if_nametoindex('en0')

#Exercise 2
import socket
socket.gethostbyname_ex('www.google.com')
socket.gethostbyname_ex('www.utexas.edu')
socket.gethostbyname_ex('www.amazon.com')

#Exercise 3
import socket
socket.gethostbyname('www.google.com')
socket.gethostbyname('www.utexas.edu')
socket.gethostbyname('www.amazon.com')

#Exercise 4
import socket
socket.gethostname()
socket.getfqdn()
