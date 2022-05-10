import socket
socket.if_indextoname(2)

ip = socket.gethostbyname('www.google.com')
print(ip)
port = 80
url = 'http://google.com'

server = (ip,port)
b = bytes(url,'UTF-8')
s.sendto(b,server)

result = s.recvfrom(4096)
print(result)

"""
