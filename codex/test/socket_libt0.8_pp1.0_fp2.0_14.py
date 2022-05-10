import socket, threading

#客户端处理函数
def handle_sock(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        #time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

#创建一个监听的socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#监听端口
s.bind(('127.0.0.1', 9999))
#开始监听,并设置最多连接
