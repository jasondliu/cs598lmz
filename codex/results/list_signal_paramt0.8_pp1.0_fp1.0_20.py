import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

while delays:
    signal.pause()
</code>
But it seems not reliable. The <code>delays</code> list could be modified during <code>signal.pause()</code> which causes unexpected intervals between alarms. So the question is how to implement this statistic for correct results.
Does it make sense to measure time and send signals to myself in the same process? Or it is better to send UDP packets to myself (localhost) and measure time on the other side? Or use something else?


A:

Use a thread to handle signals and main thread to pause
<code>import itertools
import random
import signal
import threading
import time

N = 10
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]
#delays = [0.000001, 0.000002, 0
