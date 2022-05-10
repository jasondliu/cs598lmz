import threading
# Test threading daemon
import time
import os

def daemon():
    p = os.getpid()
    print 'daemon: %s' % p
    time.sleep(2)
    print 'daemon exit'

def non_daemon():
    p = os.getpid()
    print 'non daemon: %s' % p
    print 'non daemon exit'

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()
d.join()
t.join()
