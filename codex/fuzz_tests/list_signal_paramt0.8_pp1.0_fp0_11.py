import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, 0.001)
        print "I'm still alive!"
    else:
        print "Done!"
    return True
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.001)

while delays:
    time.sleep(delays[0])
    delays = delays[1:]
print "Done!"
