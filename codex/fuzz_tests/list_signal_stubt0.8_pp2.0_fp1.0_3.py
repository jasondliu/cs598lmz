import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        with open('/dev/null', 'w') as f:
            f.write('Hello')
    else:
        with open('/dev/null', 'w') as f:
            f.write('Goodbye')

handler()
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())
while delays:
    signal.pause()
</code>

