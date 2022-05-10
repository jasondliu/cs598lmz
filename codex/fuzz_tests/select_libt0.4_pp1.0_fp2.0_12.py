import selectors
import socket
import types

# 创建一个selectors对象
sel = selectors.DefaultSelector()

# 定义一个处理请求的函数
def read(conn, mask):
    data = conn.recv(1024)
    if data:
        conn.send(data)
    else:
        sel.unregister(conn)
        conn.close()

# 创建一个socket对象
sock = socket.socket()
sock.bind(('localhost', 1234))
sock.listen(100)
sock.setblocking(False)

# 将socket对象注册到selectors中
sel.register(sock, selectors.EVENT_READ, read)

# 开始监听
while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.
