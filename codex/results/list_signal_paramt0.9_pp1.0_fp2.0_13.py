import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        print "in handler"
    else:
        print "no more events"

signal.signal(signal.SIGALRM, handler)
handler()

# should work also with:
# signal.setitimer(signal.ITIMER_REAL, delay)
# signal.signal(signal.SIGALRM, lambda: print("hi"))
# signal.setitimer(signal.ITIMER_REAL, interval)
