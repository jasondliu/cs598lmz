import select
# Test select.select
import socket
import time

t = socket.socket()
t.bind(('localhost', 54321))
t.listen(3)

r = [t]
w = []
e = []

while True:
    r, w, e = select.select(r, w, e, 60)
    print 'something happend'
    time.sleep(20)
    print 'something happend'
