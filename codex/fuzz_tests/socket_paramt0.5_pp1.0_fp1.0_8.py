import socket
socket.if_indextoname(socket.if_nametoindex('eth0'))

#10.2
import socket
socket.gethostbyname('www.baidu.com')

#10.3
import socket
socket.gethostbyname_ex('www.baidu.com')

#10.4
import socket
socket.gethostbyname_ex('www.baidu.com')[2]

#10.5
import socket
socket.gethostbyname_ex('www.baidu.com')[2][0]

#10.6
import socket
socket.gethostbyaddr('202.108.22.5')

#10.7
import socket
socket.getnameinfo(('202.108.22.5',80),0)

#10.8
import socket
socket.getservbyname('www')

#10.9
import socket
socket.getservbyport(80)

#10.10
import socket
socket.getaddrinfo('www.baidu.com',80,0,0,socket.IPPROTO_TC
