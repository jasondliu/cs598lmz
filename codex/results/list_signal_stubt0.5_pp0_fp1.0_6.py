import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print('done')
        sys.exit(0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while True:
    pass
</code>
The code above is just a proof-of-concept.  You'll want to make sure you handle the case where the user presses Ctrl+C, and you'll also want to make sure you have a way to stop the timer when you're done.

