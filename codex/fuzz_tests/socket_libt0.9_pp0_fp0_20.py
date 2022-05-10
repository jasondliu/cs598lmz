import socket
import time

HOST = ''
PORT = 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

while True:
    stream, addr = server.accept()

    timestamp = str(time.time())
    stream.sendto(timestamp.encode(), addr)

    stream.close()
