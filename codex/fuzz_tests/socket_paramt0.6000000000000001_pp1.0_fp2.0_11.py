import socket
socket.if_indextoname(3)

# socket.getaddrinfo(host, port, family=0, type=0, proto=0, flags=0)
# host: 主机名或IP地址
# port: 端口号
# family: 地址簇，默认为0，表示AF_UNSPEC，即任意地址簇
# type: 套接字类型，默认为0，表示SOCK_STREAM
# proto: 协议类型，默认为0，表示IPPROTO_IP
# flags: 通常为0，表示AI_ADDRCONFIG
socket.getaddrinfo('www.baidu.com', 'http')

# socket.gethostbyname(hostname
