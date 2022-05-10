import select
# Test select.select
import socket
import time

host = ''
port = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

conn, addr = s.accept()
print 'Connected by', addr
while True:
    time.sleep(5)
    ready = select.select([conn], [], [])
    if ready[0]:
        data = conn.recv(1024)
        if not data: break
        conn.send(data)
conn.close()
