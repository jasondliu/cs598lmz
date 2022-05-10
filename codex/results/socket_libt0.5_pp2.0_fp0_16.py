import socket
import threading
import time

# 创建socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定本地ip和端口
sock.bind(('127.0.0.1', 9999))
# 监听连接
sock.listen(5)
print('Waiting for connection...')


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


while True:
    #
