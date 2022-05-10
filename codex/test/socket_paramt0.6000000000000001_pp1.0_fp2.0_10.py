import socket
socket.if_indextoname('3')

socket.gethostbyname('www.google.com')
socket.gethostbyaddr('216.58.194.174')
socket.gethostbyname_ex('www.google.com')

socket.getprotobyname('tcp')
socket.getservbyname('http')
socket.getservbyport(80)

socket.getaddrinfo('www.google.com', 80)

socket.getnameinfo(('216.58.194.174', 80), 0)

sock = socket.socket()
sock.bind(('', 0))
sock.connect(('www.google.com', 80))
sock.listen(5)
sock.accept()
sock.send('GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n')
sock.recv(1024)
sock.close()

sock = socket.socket()
sock.connect(('www.google.com', 80))
