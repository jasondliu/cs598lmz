import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        sys.exit()

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, random.random() * 2e-5)
print('--- Running %d stochastic processes ---' % N)

ctime = 0
for t in delays:
    ctime += t
    handler()

print('Simulated time: %.5f' % ctime)
</code>
putting the emulation code in a function, replacing the signal handler with a "pop the next time off the delays queue and use it" call to signal.setitimer, and putting the call to setitimer in another "get the next time" call really turns this into a piece of readable code.
Note: I have no idea if this code is correct or not, I can't see a problem at first glance (if anyone can, I'll give you a downvote immediately), but if anyone is actually going to use this code, please run a test.

