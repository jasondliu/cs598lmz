import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('127.0.0.1', 8888))

sock.listen(5)

print('Server listening ...')

while 1:
    conn, addr = sock.accept()
    while 1:
        output = conn.recv(1024)
        if not output: break
        print(output)
        conn.send(output)

print('Server shutting down ...')

sock.close()
