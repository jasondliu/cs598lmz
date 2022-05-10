import select
# Test select.select()

import socket

host = ''
port = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

conn, addr = s.accept()
print('Connected by', addr)

while 1:
    try:
        data = conn.recv(1024)
    except socket.error as e:
        print('Error receiving data: %s' % e)
        # conn.close()
        # s.close()
        # break
    if not data:
        break
    conn.sendall(data)

conn.close()
