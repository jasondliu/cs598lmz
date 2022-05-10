import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, delays.pop())

try:
    while delays:
        signal.pause()
except KeyboardInterrupt:
    print('{} signals were still pending'.format(len(delays)))
</code>

Edit: added code to process remaining pending signals when <code>Ctrl-C</code> is pressed.

<blockquote>
<p>this is not very precise, I need to get the time at which the signal was emitted</p>
</blockquote>
The previous code is precisely what you asked for.
The reason you observe such imprecision is that the system can have many other things to do, that may delay your signal by a lot.

