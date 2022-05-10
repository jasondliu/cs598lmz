import socket
socket.if_indextoname('3')

result = socket.getaddrinfo('www.python.org', 'http')
type(result), len(result)
type(result[0]), result[0]
