import socket
socket.if_indextoname(1)

#%%
# 创建一个UDP套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口和地址
sock.bind(('127.0.0.1', 5555))

# 设置套接字选项
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 获取套接字选项的值
sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)

#%%
# 创建一个TCP套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置套接字选项
