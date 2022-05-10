import socket
import time

#HOST = 'localhost' # Symbolic name meaning all available interfaces
HOST = '192.168.1.101'
PORT = 50007 # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((HOST,PORT))
s.bind((HOST,PORT))
s.listen(1)

conn, addr = s.accept()
print "Connected by " + str(addr)

is_active = True

last_time_recieved = time.time()

while is_active:
    data = conn.recv(1024)
    print data
    if not data: 
        break
    conn.send(data)

conn.close()
