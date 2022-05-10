import socket
socket.if_indextoname(15)

r = 'http://www.python.org/fish.html'

print(r.split('fish')[0])
print(r.split('fish')[1])

print(urllib.parse.unquote(r))

print(urllib.parse.urlparse(r))
