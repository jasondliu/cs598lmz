import select
import time
import msvcrt

"""
socket.socket 创建实例
socket.AF_INET 创建ipv4
socket.SOCK_STREAM 创建tcp套接字
"""

"""
socket.bind() 绑定地址
socket.listen() 监听
socket.accept() 接受连接
"""

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)  # 设置为非阻塞模式，在非阻塞模式下，accept()会立即返回，如果没有连接，会抛出一个异常
server.bind(('localhost', 6666))
server.list
