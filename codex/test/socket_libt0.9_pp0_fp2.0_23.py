import socket 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8080))
sock.listen(5)

while True:
    newSocket, addr = sock.accept()
    while True:
        recvData = newSocket.recv(1024)
