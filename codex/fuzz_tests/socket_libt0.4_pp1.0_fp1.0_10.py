import socket
import threading
import time
import sys

# 基本的な設定
listen_port = 50000
max_msg_size = 1024

# 接続要求を処理するスレッド
def process_client_connection(connection):
    request = connection.recv(max_msg_size)
    print(request.decode())
    response = b'Hello world\n'
    connection.sendall(response)
    connection.close()

# リスニングソケットを作成
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', listen_port))
server.listen(1)
print('Listening at', server.getsockname())

while True:
    # 接続要求を処理
    connection, client_address = server.accept()
    thread = threading.Thread(target=process_client_connection, args=(connection,))
   
