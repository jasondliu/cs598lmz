import socket
socket.if_indextoname(3)

#endpoint, linux, index

s = socket.socket(socket.AF_INET, socket.SOCK_RAW)
socket.socket.bind(s, socket.if_indextoname(3))
data = s.recv(4096)

start = data.find(b'\xff\xd8')
end = data.find(b'\xff\xd9')

jpef = data[start:end+2]

f = open('1.jpeg', 'wb')
f.write(jpeg)
f.close()


import socket
socket.if_indextoname(3)
#endpoint, linux, index

s = socket.socket(socket.AF_INET, socket.SOCK_RAW)
socket.socket.bind(s, socket.if_indextoname(3))
data = s.recv(4096)

start = data.find(b'\xff\xd8')
end = data.find(b'\xff\xd9')

