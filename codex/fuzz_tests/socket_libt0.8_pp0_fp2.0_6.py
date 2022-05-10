import socket

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
s.connect(('127.0.0.1', 1234))

while True:
    daten = input()
    if daten == 'quit':
        break
    s.send(daten.encode())
    data = s.recv(1024)
    print(data.decode())

s.close()
