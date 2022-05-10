import socket
socket.if_indextoname(3)

# 获取网络接口的状态
socket.if_up('lo')
socket.if_up('eth0')

# 获取网络接口的地址
socket.if_addr('lo')
socket.if_addr('eth0')

# 获取网络接口的广播地址
socket.if_broadcast('lo')
socket.if_broadcast('eth0')

# 获取网络接口的网络地址
socket.if_netmask('lo')
socket.if_netmask('eth0')

# 获取网络接口的硬件地址
socket.if_hwaddr('lo')
socket.if_hwaddr('eth0')

# 获取网
