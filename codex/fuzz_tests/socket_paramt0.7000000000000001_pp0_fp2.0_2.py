import socket
socket.if_indextoname(1)
#'en0'

#3.2.4 在给定的套接字上调用 connect()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com.cn', 80))

#3.2.5 在套接字上调用 send() 和 recv()
#创建一个面向流的 TCP 服务器
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#监听端口:
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('Waiting for connection...')
while True:
    #接受一个新连接:
    sock, addr = s.accept()
    #创建新线
