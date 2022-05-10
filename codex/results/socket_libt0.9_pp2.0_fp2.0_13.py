import socket
import _thread
import sys

BUF_SIZE = 1024
PORT = 12345

def client_target(conn, addr):
    file_name = conn.recv(BUF_SIZE).decode()
    file_size = conn.recv(BUF_SIZE)

    print('Client:',addr)
    print('File name:',file_name)
    print('File size:',file_size.decode())

    recv_size = 0
    file = open(file_name, 'wb')
    print('Start receiving:')
    while (int)(file_size.decode()) > recv_size:
        if (int)(file_size.decode()) - recv_size > BUF_SIZE:
            size = BUF_SIZE
        else:
            size = (int)(file_size.decode()) - recv_size
            print('Received:',recv_size)
        data = conn.recv(size)
        recv_size += len(data)
        file.write(data)
    file.close()

