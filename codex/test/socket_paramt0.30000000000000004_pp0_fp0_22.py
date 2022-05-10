import socket
socket.if_indextoname(3)

# 创建一个TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 使用socket绑定到端口
server_address = ('localhost', 10000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

# 使用socket监听传入的连接
sock.listen(1)

while True:
    # 等待一个连接
    print('waiting for a connection')
    connection, client_address = sock.accept()
