import socket
socket.if_indextoname(3)

#Encontrar la direccion ip del host en linux
hostname = socket.gethostname()
socket.gethostbyname(hostname)

#Conocer la direccion IP sepudieron encontrar
socket.getaddrinfo('google.com', 80)
