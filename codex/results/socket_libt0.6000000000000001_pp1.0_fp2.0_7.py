import socket

# ip = 'localhost'
# port = 6666
# addr = (ip, port)

# client = socket.socket()
# client.connect(addr)

# while True:
#     data = input('>> ')
#     if not data:
#         break
#     client.send(data.encode('utf-8'))
#     msg = client.recv(1024)
#     print('收到服务器的数据:', msg.decode('utf-8'))

# client.close()

# 公共部分
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 6666))

# 接收欢迎信息
print(s.recv(1024).decode('utf-8'))

for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据
    s
