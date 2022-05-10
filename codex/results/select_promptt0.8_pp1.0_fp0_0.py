import select
# Test select.select()

print 'starting'

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 1))
s.listen(1)
s.setblocking(0)
#s.settimeout(0.0)

import threading
import time

class MyThread(threading.Thread):
    def run(self):
        time.sleep(10)
        print 'recv'
        s.recv(10)
        print 'recv done'

thread = MyThread()
thread.daemon = True
thread.start()

for attempt in xrange(3):
    print 'selecting'
    r, w, x = select.select([s], [], [], 2.0)
    print 'select done.', r
