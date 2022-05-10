import select
# Test select.select() & select.poll() 
# Refer to : http://stackoverflow.com/questions/2719017/how-to-set-timeout-on-pythons-socket-recv-method
#
import socket
import sys

port = 4444
host = 'localhost'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setblocking(0)
s.bind(("", 0))
s.sendto("client request", (host, port))
input = [s]

while 1:
    i, o, e = select.select(input, [], [])
    for x in i:
        if x == s:
            print "received data: ", x.recv(1024)
            print "recvfrom(0) : ", x.recvfrom(0)
            print "recvfrom(128) : ", x.recvfrom(128)
            print "recv(0) : ", x.recv(0)
            print "recv(128) : ", x.recv(128
