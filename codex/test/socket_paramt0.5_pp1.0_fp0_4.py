import socket
socket.if_indextoname(3)

# gethostbyname(hostname)
# Return the IP address (a string of the form '255.255.255.255') for a host.

import socket
socket.gethostbyname('www.baidu.com')

# gethostbyname_ex(hostname)
# Return a triple (hostname, aliaslist, ipaddrlist) where hostname is the primary host name responding to the given ip_address, aliaslist is a (possibly empty) list of alternative host names for the same address, and ipaddrlist is a list of IP addresses for the same interface on the same host (often but not always a single address).

import socket
socket.gethostbyname_ex('www.baidu.com')

# gethostbyaddr(ip_address)
# Return a triple (hostname, aliaslist, ipaddrlist) where hostname is the primary host name responding to the given ip_address, aliaslist is a (possibly empty) list of alternative host names for the same address, and ipaddrlist is a list of IP addresses for the same interface on the same host (most likely containing only
