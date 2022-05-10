import socket
socket.if_indextoname(1)

# Get the name of a network interface given its index.

socket.if_nametoindex('lo')

# Get the index of a network interface given its name.

socket.if_nameindex()

# Get the list of network interfaces available on the system.

socket.if_nameindex()[0][1]

# Get the name of the first network interface.

socket.gethostbyname('localhost')

# Get the IP address of a hostname.

socket.gethostname()

# Get the hostname of the machine the script is running on.

socket.getfqdn()

# Get the fully qualified domain name of the machine the script is running on.

socket.getaddrinfo(socket.getfqdn(), None)

# Get all the IP addresses of the machine the script is running on.

socket.getaddrinfo('www.python.org', 'http')

# Get the IP address of a hostname.

socket.getaddrinfo('www.python.org', 'http', 0, socket.SOCK_STREAM,
