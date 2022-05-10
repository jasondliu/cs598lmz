import socket
socket.if_indextoname(1)

# Create an interface name
socket.if_nameindex()

# Convert interface name to index
socket.if_nametoindex('lo')

# Get socket addresses
socket.getaddrinfo('www.python.org', 'http')

# Get hostname
socket.gethostname()

# Get host by name
socket.gethostbyname('localhost')

# Get host by name with aliases
socket.gethostbyname_ex('localhost')

# Get host by address
socket.gethostbyaddr('127.0.0.1')

# Get service by port and protocol name
socket.getservbyport(80, 'tcp')

# Get service by port and protocol number
socket.getservbyport(80, socket.IPPROTO_TCP)

# Get protocol number
socket.getprotobyname('tcp')

# Get protocol name
socket.getprotobyname('ip')

# Get the default socket timeout value
socket.getdefaulttimeout()

# Set the default socket timeout value
socket.setdefaulttimeout(10)

