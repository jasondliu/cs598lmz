import socket
socket.if_indextoname(12)

#实现跨平台查询
import sys
if sys.platform.startswith('win'):
    print(socket.if_indextoname(11))
else:
    print(socket.if_indextoname(1))

#其它网络操作
#socket.socketpair(family=AF_INET, type=SOCK_STREAM, proto=0)       本地协议族
#socket.inet_aton(ip_string)                                      点分十进制字符串 变二进制表示
#socket.inet_ntoa(packed_ip)                                      将二进制表示的ip地址 变成点分十进制字符串

#socket.gethostbyname_ex(hostname)
#socket.gethostname()


