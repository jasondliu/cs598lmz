import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        print "Slept for %f seconds" % (1e6 * signal.getitimer(signal.ITIMER_REAL)[0])
    else:
        print "Done"
        sys.exit(0)


signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

handler()

while True:
    pass
