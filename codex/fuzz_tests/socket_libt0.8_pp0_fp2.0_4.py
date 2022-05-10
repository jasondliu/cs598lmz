import socket
import threading
import cv2

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.0.12', 80 )
server_socket.bind(server_address)
server_socket.listen(1)
client,addr = server_socket.accept()

print ('connected')

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

while True:
    image_len = recvall(client, 16)
    if (not image_len): break
    image_stream = io.BytesIO()
    image_stream.write(recvall(client, image_len))
    image_stream.seek(0)
    image = Image.open(image_stream)
    print('Image is %dx%d' % image.size)
    image.verify()

