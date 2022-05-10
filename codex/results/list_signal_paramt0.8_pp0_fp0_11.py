import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

signal.setitimer(signal.ITIMER_REAL, 0)
signal.signal(signal.SIGALRM, handler)
handler()

while delays:
    signal.pause()
</code>
I'm on Mac OS X 10.8.2, and I see a delay of about 0.5 ms between each SIGALRM. If I try to generate more than about 700,000 SIGALRM per second, I see my CPU usage jump to 40% and my system slows down terribly.
I'm clearly doing something wrong, but I can't figure out what.
Edit: 
Using <code>signal.sigtimedwait()</code> instead of <code>signal.pause()</code>:
<code>import signal
import random

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

for delay in delays:
    signal.setitimer(signal.ITIMER_REAL, delay)
    signal
