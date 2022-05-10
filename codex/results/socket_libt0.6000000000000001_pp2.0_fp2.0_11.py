import socket

# 实例化一个socket对象
server = socket.socket()
# 绑定服务器的ip地址和端口号
server.bind(('localhost', 8888))
# 服务器监听
server.listen()

# 接收请求
conn, addr = server.accept()
# 获取客户端的请求数据
data = conn.recv(1024)
print(data.decode('utf-8'))
# 发送响应数据
conn.send(data.upper())

# 关闭连接
conn.close()
server.close()
