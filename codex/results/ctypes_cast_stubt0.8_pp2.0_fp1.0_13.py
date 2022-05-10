import ctypes
ctypes.cast()
import json
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.0.101', 8089))

while(True):
    data = s.recv(1024)
    str1 = data.decode('utf-8')
    print(str1)
    if not data:
        break

    # s.send(b'\x01\x64\x00\x00')
    # data = s.recv(1024)
    # print(data)
    # s.send(b'\x02\x64\x00\x00')
    # data = s.recv(1024)


s.close()
