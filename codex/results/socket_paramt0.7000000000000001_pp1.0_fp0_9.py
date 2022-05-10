import socket
socket.if_indextoname(1)

# If no such interface exists, an error is raised.

# socket.if_nametoindex(if_name)
# Translate an interface name to an index, e.g. ‘eth0’ to 3.

# socket.getnameinfo(sockaddr, flags)
# Translate a socket address sockaddr into a 2-tuple (host, port). Depending on the settings of flags, the result can contain a numerical host address or the host name, a textual service name or port number.

# socket.getaddrinfo(host, port, family=0, type=0, proto=0, flags=0)
# Translate the host/port argument into a sequence of 5-tuples that contain all the necessary arguments for creating a socket connected to that service.

# The host argument can be a string representing either a hostname in Internet domain notation like 'daring.cwi.nl' or an IPv4 address like '100.50.200.5', or it can be an IPv6 address in colon-separated hexadecimal notation like '2001:db8:8714:3a90::
