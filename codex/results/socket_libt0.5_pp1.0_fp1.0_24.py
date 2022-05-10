import socket
import sys
import threading

# 需要绑定的ip和端口
bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定ip和端口到socket
server.bind((bind_ip, bind_port))

# 最大连接数
server.listen(5)

print("[*] Listening on %s:%d" % (bind_ip, bind_port))

# 客户端处理线程


def handle_client(client_socket):
    # 打印出客户端发送的内容
    request = client_socket.recv(1024)
    print("[*] Received: %s" % request)
    # 向客户端返回一个
