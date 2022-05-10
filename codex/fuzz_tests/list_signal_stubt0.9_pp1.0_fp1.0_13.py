import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        with open('/tmp/data.txt', 'w') as f:
            for i in range(N):
                f.write("{}\n".format(i * 2e-5))
        sys.exit()

signal.signal(signal.SIGALRM, handler)
handler()
signal.pause()
