import sys, threading

def run():
    #创建一个新连接tcp服务器
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', 9001))
    server.listen(10)
    try:
        while True:
            conn, address = server.accept()
            print(address)
            request = conn.recv(1024)
            response = 'hello client'
            conn.sendall(bytes(response, 'utf8'))
    except KeyboardInterrupt:
        print('Server shutdown')
        server.close()

t1 = threading.Thread(target=run)
t1.start()

while True:
    time.sleep(1)
    pass
