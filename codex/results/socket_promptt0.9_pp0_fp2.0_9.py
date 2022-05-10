import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(3))
# Returns: 'en0'

# Test socket.if_nametoindex()
print(socket.if_nametoindex('en0'))
# Returns: 3

# Test socket.setdefaulttimeout()
socket.setdefaulttimeout(10.0)

# Test socket.gethostbyname()
print(socket.gethostbyname('localhost'))
# Returns: '127.0.0.1'

print(socket.gethostbyname('6.6.6.6'))
# Returns: '6.6.6.6'

print(socket.gethostbyname('invalid.hostname'))
# Returns: the IP address of the local host

# Test socket.gethostbyname_ex()
print(socket.gethostbyname_ex('localhost'))
# Returns: ('127.0.0.1', ['localhost'], ['127.0.0.1'])

print(socket.gethostbyname_ex('www.python.org'))
# Returns: ('
