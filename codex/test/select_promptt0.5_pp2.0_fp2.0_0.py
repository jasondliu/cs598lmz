import select
# Test select.select()

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8080))

while True:
    readable, _, _ = select.select([s], [], [])
    if readable:
        data = s.recv(1024)
        if not data:
            break
        print(data.decode('utf-8'))

s.close()
