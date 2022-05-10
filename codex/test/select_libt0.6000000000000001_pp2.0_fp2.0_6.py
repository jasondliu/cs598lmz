import select
import sys
import os

srv_ip = '0.0.0.0'
srv_port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((srv_ip, srv_port))

s.listen(1)

while True:
    conn, addr = s.accept()
    print('Client connected from', addr)
    # data = conn.recv(4096)
    # print(data)
    # conn.sendall(data)
    # conn.close()

    # conn.setblocking(0)
    # data = b''
    # while True:
    #     part = conn.recv(1024)
    #     data += part
    #     if len(part) < 1024:
    #         break
    # if data:
    #     conn.sendall(data)
    # conn.close()
