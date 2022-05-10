import socket
socket.if_indextoname(33)

#To get the index number of an interface, use:
import socket
socket.if_nametoindex('eth2')

#To get the name of the interface to which a socket is bound, use:
import socket
soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.bind(('1.1.1.1', '10'))
socket.if_nameforindex(soc.fileno())

# getfqdn() supports an optional argument and returns the fully qualified domain name
# (FQDN) of the host. If the optional argument is a string:

#If the string is a hostname, the function will return the FQDN. If the hostname is not
#found in any of the DNS nameservers, a ValueError exception will be thrown.

#If the string is an IP address, the function will return the FQDN if the IP address is
#found in one of the DNS nameservers. Otherwise, it will return the IP address itself.
#To find out if a name or IP address is a DNS alias, get
