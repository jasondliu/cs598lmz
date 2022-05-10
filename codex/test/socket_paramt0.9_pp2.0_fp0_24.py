import socket
socket.if_indextoname(3)

#6.26
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
max_size = 8192
msg = b'1'*max_size
while len(msg):
    sent = s.send(msg)
    msg = msg[sent:]

print('Message size:', len(msg))

#6.27
import time
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
now = time.ctime(time.time())
s.sendto(now.encode(), (host, port))
print('Client waiting')

rec_data,address = s.recvfrom(max_size)
print('Server', rec_data)
s.close()

#6.28
import time
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#host = socket.gethostname()
host = 'localhost'
port = 12345
s.bind((host,port))
