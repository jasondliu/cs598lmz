import select
import socket
import queue
import os

# 创建一个套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置为非阻塞
s.setblocking(False)
# 绑定地址
s.bind(('127.0.0.1', 5000))
# 监听
s.listen(5)
# 创建一个epoll对象
epoll = select.epoll()
# 注册要监听的文件描述符
epoll.register(s.fileno(), select.EPOLLIN)
# 字典，用来保存文件描述符和对象的对应关系
fd_to_socket = {s.fileno(): s, }
#
