import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))
# Test socket.if_nameindex()
print(socket.if_nameindex())

# Test socket.gethostbyname()
print(socket.gethostbyname("localhost"))
print(socket.gethostbyname("google.com"))
print(socket.gethostbyname("www.google.com"))

# Test socket.gethostbyname_ex()
print(socket.gethostbyname_ex("localhost"))
print(socket.gethostbyname_ex("google.com"))
print(socket.gethostbyname_ex("www.google.com"))

# Test socket.gethostbyaddr()
print(socket.gethostbyaddr("127.0.0.1"))
print(socket.gethostbyaddr("8.8.8.8"))
print(socket.gethostbyaddr("216.58.194.174"))

# Test socket.gethostname()
print(socket.gethostname())

# Test socket.gethostname()
print(socket.gethostname())

#
