import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while delays:
    time.sleep(1.0)
</code>
The main problem with this script is that handling a signal is not an atomic operation.  If the signal is received while the program is updating a global variable, it is possible that the signal handler will see the intermediate state of the update.  This problem can be avoided by having the signal handler be the only code that updates the global variables.

