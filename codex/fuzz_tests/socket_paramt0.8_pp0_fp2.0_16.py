import socket
socket.if_indextoname(1)

socket.if_nametoindex("en0")

socket.if_nameindex()

socket.gethostname()

socket.getfqdn("192.168.1.1")

socket.gethostbyname("127.0.0.1")

socket.gethostbyaddr("127.0.0.1")

socket.gethostbyname_ex("www.baidu.com")

socket.gethostbyname_ex("www.qq.com")

socket.gethostbyname_ex("www.csdn.net")

#coding=utf-8  
import socket  
  
# 创建 socket 对象  
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
  
# 获取本地主机名  
host = socket.gethostname()  
  
port = 9999  
  
# 绑定端口号  
serversocket.bind((
