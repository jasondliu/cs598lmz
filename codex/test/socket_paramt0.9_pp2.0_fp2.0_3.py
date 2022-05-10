import socket
socket.if_indextoname(2)

# 有些使用的的套接字并非 IPV4 协议
import socket
socket.if_indextoname(3)

# socket 合并
# 早先需要五个函数来找到套接字地址，一个函数 需要承担两个对象方法
import socket
socket.getfqdn('8.8.8.8')

#	dsn = socket.getaddrinfo(host, port)
	# 然后根据套接字描述找到地址

# 对于本地 IP 地址 127.0.0.1 会变转为主机名
import socket
