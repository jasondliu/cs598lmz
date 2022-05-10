import socket
socket.if_indextoname(3)

#hostname = socket.gethostname()
#print(hostname)

#print(socket.gethostbyname(hostname))

import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
    html = response.read()

print(html)
