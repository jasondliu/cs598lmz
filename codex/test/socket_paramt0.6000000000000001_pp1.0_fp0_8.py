import socket
socket.if_indextoname('6')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8080))
s.listen(1)

while True:
    conn, addr = s.accept()
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data: break
        conn.send(data)
    conn.close()

'''
> nc 127.0.0.1 8080
Hello World
Hello World
^C
'''
