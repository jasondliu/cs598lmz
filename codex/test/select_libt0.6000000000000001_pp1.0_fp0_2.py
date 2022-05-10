import select
import socket
import sys

# 服务器地址
HOST = '127.0.0.1'
PORT = 8888

# 创建一个流式套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置套接字选项
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 将套接字绑定到地址
sock.bind((HOST, PORT))
# 启动监听（最大连接数为5）
sock.listen(5)

# 与客户端通信
