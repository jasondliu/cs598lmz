import socket
# Test socket.if_indextoname(1)
# If a wired ethernet connection is present the output should be 'eth0'
[socket.if_indextoname(1),
 socket.if_indextoname(32),
 socket.if_indextoname(45),
 socket.if_indextoname(97)]

# Test socket.if_nameindex()
# It lists the interface name and index
socket.if_nameindex()

# Test socket.if_nametoindex()
# Give the interface name as input to get the index
socket.if_nametoindex('wlan0')
socket.if_nametoindex('eth0')

# Test socket.gethostname()
# It returns the hostname if it can resolve
# If it cannot resolve, it throws OSError
socket.gethostname()
socket.gethostname()

# Test socket.getfqdn()
# It returns the fully qualified domain name
# If it cannot resolve, it throws OSError
socket.getfqdn()
# Test socket.gethostbyname()
# If IP6 is enabled by default
