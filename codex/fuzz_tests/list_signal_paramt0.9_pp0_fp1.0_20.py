import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
</code>
If you've missed the signal at 1000000 then you're already late.

Edit: If what you're trying to do is reliably measure 1000000 nanoseconds per signal, then there's no need to set up a timer. Just set a signal handler, and in this signal handler, do whatever your processing is, then, in the signal handler itself, recursively set a new signal handler and raise SIGALRM, and then it'll just keep being raised recursively until something goes wrong.
<code>import signal

def handler():
    try:
        #do anything

        signal.signal(signal.SIGALRM, handler)
        raise signal.SIGALRM
    except:
        #handle stack overflow

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIM
