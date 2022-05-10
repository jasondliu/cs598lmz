import socket
import time
import threading

# 创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机名
host = socket.gethostname()
port = 9999
# 连接服务，指定主机和端口
s.connect((host, port))

def recv_msg(s):
    while True:
        # 接收小于1024字节的数据
        msg = s.recv(1024)
        print(msg.decode('utf-8'))

def send_msg(s):
    while True:
        msg = input('>>: ').strip()
        if len(msg) == 0:continue
        s.send(msg.encode('utf-8'))

t1 = threading.Thread(target=recv_msg, args=(s,))
