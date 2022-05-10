import socket,sys
import time

host = '192.168.1.8'
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print "Socket Created"

try:
    s.bind((host,port))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

s.listen(10)
print 'Socket now listening'

conn, addr = s.accept()

print 'Connected with ' + addr[0] + ':' + str(addr[1])

while 1:

    data = conn.recv(1024)
    #conn.sendall(data)
    if not data:
        break
    outfile = open('myfile.txt','a')
    outfile.write(data)
    print data
