import socket
socket.if_indextoname("2")

socket.gethostname()

socket.gethostbyname("www.educode.cn")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("172.19.74.12", 10086))
# 设置socket不阻塞
s.setblocking(False)
# 设置套接字选项值
s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 23)
# 获得套接字选项值
s.getsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE)

# 接受连接
s.listen(5)

while True:
    conn = None
    try:
        conn, addr = s.accept()
        conn.setblocking(False)
        conn.settimeout(5)
        cdata =
