import socket
socket.if_indextoname(3)

#绑定接口
s.bind(('192.168.0.1',8080))

#监听
s.listen(5)

#接收客户端连接
conn,addr = s.accept()

#接收客户端发送的数据
data = conn.recv(1024)
print(data)

#发送数据给客户端
conn.send(b'hello')

#关闭连接
conn.close()
