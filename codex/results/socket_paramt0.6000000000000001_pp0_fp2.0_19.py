import socket
socket.if_indextoname(if_index)

#The following code will return the IPv4 address corresponding to the interface name given as argument.
import socket
socket.gethostbyname('www.python.org')

#The following code will return the IPv4 address corresponding to the interface name given as argument.
import socket
socket.gethostbyname_ex('www.python.org')

#The following code will return the IPv6 address corresponding to the interface name given as argument.
import socket
socket.getaddrinfo('www.python.org', 80)

#The following code will return the IPv6 address corresponding to the interface name given as argument.
import socket
socket.getaddrinfo('www.python.org', 80, socket.AF_INET6)

#The following code will return the IPv4 address corresponding to the interface name given as argument.
import socket
socket.getaddrinfo('www.python.org', 80, socket.AF_INET)

#The following code will return the IPv4 address corresponding to the interface name given as argument.
import socket
socket.getaddrinfo('www.python.org', 80, socket.
