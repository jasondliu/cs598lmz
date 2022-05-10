import socket
socket.if_indextoname(3)

#import the module

import socket

#create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to a server
s.connect(("www.sina.com.cn", 80))

#send data
s.send(b"GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n")

#receive data
buffer = []
while True:
    #receive data by 1024 bytes
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

#close the socket
s.close()

#receive the header and the html
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))

#save the html to a file
