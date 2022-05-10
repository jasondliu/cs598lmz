import socket
socket.if_indextoname(2)

# gethostname() : Returns the hostname of the machine where the Python interpreter is currently executing.
import socket
socket.gethostname()

# gethostbyname() : Takes a hostname string as an argument, and returns the IP address of the host.
import socket
socket.gethostbyname('www.linkedin.com')

# gethostbyaddr() : Takes a host IP address as an argument, and returns the hostname of the host.
import socket
socket.gethostbyaddr('162.246.157.99')

# gethostbyname_ex() : Takes a hostname string as an argument, and returns a tuple containing the hostname,
#                      alias list, and IP address of the host.
import socket
socket.gethostbyname_ex('www.linkedin.com')

# getfqdn() : Takes a hostname as an argument, and returns the Fully Qualified Domain Name.
import socket
socket.getfqdn('www.linkedin.com')

# getaddrinfo() : Takes a hostname and port number as arguments, and returns a list of
