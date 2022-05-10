import socket
# Test socket.if_indextoname()
for name in socket.if_nameindex():
    print(name)

print(socket.gethostbyaddr('8.8.8.8'))

print(socket.gethostbyname('www.google.com'))

net_name, alias, ip_address = socket.gethostbyname_ex('www.google.com')
print(net_name, alias, ip_address)

print(socket.gethostname())

print(socket.gethostbyaddr('127.0.0.1'))

print(socket.gethostbyname('localhost'))

print(socket.gethostbyname_ex('localhost'))

print(socket.gethostbyname_ex('google.com'))

print(socket.gethostbyname_ex('google.com')[2])

print(socket.gethostbyname_ex('google.com')[2][0])

print(socket.gethostbyaddr('127.0.0.1'))

print(socket.gethostbyname('localhost'))

