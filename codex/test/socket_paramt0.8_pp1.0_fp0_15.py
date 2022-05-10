import socket
socket.if_indextoname(4)

# Клиент
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9090))
s.send('hello server'.encode())
data = s.recv(1024)
s.close()
print('received: ', data.decode())

# Сервер
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9090))
s.listen(1)
conn, addr = s.accept()
print('connected: ', addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())
conn.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9090))
s.send('hello server'.encode())
data = s.recv(1024)
