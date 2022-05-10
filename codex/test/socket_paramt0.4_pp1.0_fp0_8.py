import socket
socket.if_indextoname(3)

# Find the IP address of a network interface
import socket
socket.if_nameindex()

# Get the current hostname
import socket
socket.gethostname()

# Resolve a hostname to IPv4 address format
import socket
socket.gethostbyname('google.com')

# Resolve a hostname to IPv6 address format
import socket
socket.gethostbyname_ex('google.com')

# Resolve a hostname to IPv4 address format and extended information
import socket
socket.gethostbyname_ex('google.com')

# Resolve a hostname to IPv6 address format and extended information
import socket
socket.gethostbyname_ex('google.com')

# Resolve IPv4 and IPv6 addresses for a hostname
import socket
socket.getaddrinfo('google.com', 80)

# Resolve IPv4 and IPv6 addresses for a hostname using a custom socket
import socket
