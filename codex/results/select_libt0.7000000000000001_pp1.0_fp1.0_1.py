import selectors
import socket
import sys

# 监听的端口
server_address = ('127.0.0.1', 10000)

# 建立一个selectors对象
sel = selectors.DefaultSelector()

# 建立一个socket对象
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 使得socket进程结束后可以立即重启
lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 绑定IP和端口
lsock.bind(server_address)
# 监听
lsock.listen()
print('listening on', server_address)
# 注册socket，指定监听类型为读
lsock.setblocking(False)
sel.
