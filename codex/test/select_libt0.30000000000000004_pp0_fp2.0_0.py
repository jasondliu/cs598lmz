import selectors
import socket
import types
import sys

# 创建一个selectors对象
sel = selectors.DefaultSelector()

# 创建一个服务器端的socket对象
host = 'localhost'
port = 65432
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()
print('listening on', (host, port))
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)

# 定义一个处理客户端请求的函数
def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print('accepted connection from', addr)
    conn.setblocking(False)
