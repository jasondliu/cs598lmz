import socket
# Test socket.if_indextoname()
try:
    # Python 3.8+
    socket.if_indextoname(22)
except AttributeError:
    # Python <3.8  (OSX)
    import netifaces as ni

    ni.if_indextoname(22)

# Test socket.if_nameindex()
socket.if_nameindex()

# Test socket.if_nametoindex()
socket.if_nametoindex(ni.gateways()['default'][ni.AF_INET][1])

# Test socket.sethostname()
try:
    socket.sethostname('localhost')
except OSError:
    pass

# Test socket.gethostname()
socket.gethostname()

# Test socket.gethostbyname()
socket.gethostbyname('localhost')

# Test socket.getfqdn()
socket.getfqdn()

# Test socket.getservbyname()
socket.getservbyname('telnet')

# Test socket.getservbyport()
socket.getservbyport(23
