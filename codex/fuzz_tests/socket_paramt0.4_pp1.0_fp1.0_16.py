import socket
socket.if_indextoname(1)

# 创建客户端socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接服务器
client.connect(('127.0.0.1', 8080))
# 发送数据
client.send(b'hello')
# 接收数据
data = client.recv(1024)
print(data)
# 关闭socket
client.close()
