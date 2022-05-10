import select
# Test select.select

from select import *
res = select([],[],[])
print res
print "-=" * 30


from select import select
import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = '-' * 30
print "Server is running, waiting for data."

# recvfrom( ) is a blocking function.
serv.bind(('', 8888))
serv.setblocking(0)
while True:  
    result = select([serv],[],[])
    msg, addr = result[0][0].recvfrom(1024)
    print "Message from: ", addr
    print "Message: ", msg
    print data


#Code
from select import select
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('', 0))

s.setblocking(0)

print "Before:\t", s.recvfrom(1)

print select([s],[],[])

print "After:\t", s.recvfrom(1)
