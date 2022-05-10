import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        print "PID: {}".format(os.getpid())

signal.signal(signal.SIGREAL, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while 1:
    time.sleep(2)
