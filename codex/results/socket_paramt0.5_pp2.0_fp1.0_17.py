import socket
socket.if_indextoname(3)

# 创建套接字
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 主机名和端口号
server_address = ('localhost', 10000)
print('connecting to %s port %s' % server_address)
s.connect(server_address)

# 发送数据
try:
    message = b'This is the message. It will be repeated.'
    print('sending %s' % message)
    s.sendall(message)

    # 接收数据
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = s.recv(16)
        amount_received += len(data)
        print('received %s' % data)

finally:
    print('closing socket')
    s.close()

# 服务器

