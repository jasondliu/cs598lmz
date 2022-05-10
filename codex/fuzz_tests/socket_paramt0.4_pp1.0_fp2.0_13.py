import socket
socket.if_indextoname(3)

# 获取某个网卡的掩码
socket.inet_ntoa(socket.inet_aton('192.168.1.1'))

# 获取某个网卡的广播地址
socket.inet_ntoa(socket.inet_aton('192.168.1.1') | ~ socket.inet_aton('255.255.255.0'))

# 获取某个网卡的网络地址
socket.inet_ntoa(socket.inet_aton('192.168.1.1') & socket.inet_aton('255.255.255.0'))

# 获取某个网卡的子网掩码
socket.inet_ntoa(socket.inet_aton('192.168.1.1') & socket.inet_aton('255.255.255.0'))


