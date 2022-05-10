import signal
# Test signal.setitimer()

import signal
import time

def handler(signo, frame):
    print 'got signal: ', signo
    print 'time is: ', time.ctime()
    signal.setitimer(signal.ITIMER_REAL, 2)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 2)
print 'waiting signal'
time.sleep(20)
print 'done'
