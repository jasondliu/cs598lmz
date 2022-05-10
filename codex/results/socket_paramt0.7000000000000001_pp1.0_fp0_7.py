import socket
socket.if_indextoname('3')

# We can also get the MAC address of the interface
# by using the getnode() method of the UUID module.
import uuid
uuid.getnode()

# The gethostbyname() function requires a hostname
# as its argument, and it returns a string containing
# the IP address in dotted-quad format.
socket.gethostbyname('www.python.org')

# The gethostbyname_ex() function is similar to the
# gethostbyname() function, but it returns a tuple
# containing the hostname, a list of aliases, and a
# list of IP addresses, instead of just the IP address.
socket.gethostbyname_ex('www.python.org')

# The gethostname() function simply returns the hostname
# of the machine on which the Python interpreter is running.
socket.gethostname()

# The getfqdn() function returns the fully qualified
# domain name for the machine on which the Python
# interpreter is running.
socket.getfqdn()

# The gethostbyaddr() function takes an IP address in

