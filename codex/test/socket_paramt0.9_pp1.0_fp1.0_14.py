import socket
socket.if_indextoname(63)
 
socket.socket()
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
s.bind(('', 80))
 
s.listen()
 
(conn, addr) = s.accept()
 
conn.send(b'''\
HTTP/1.0 200 OK
 
Hello world!
''')
 
conn.close()
