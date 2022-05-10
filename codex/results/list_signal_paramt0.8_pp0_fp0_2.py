import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_VIRTUAL, delays.pop(0))
    else:
        print "Done"
        sys.exit(0)

start = time.time()
signal.signal(signal.SIGVTALRM, handler)
handler()
signal.pause()
