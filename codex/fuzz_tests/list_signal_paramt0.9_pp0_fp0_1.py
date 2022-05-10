import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0), 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(0), 0)

while True:
    time.sleep(1)
    print('timers: %3d ; remaining: %.1f seconds' % (len(delays), sum(delays)))
</code>
I see the following output:
<code>timers:  158 ; remaining: 0.2 seconds
timers:  137 ; remaining: 0.2 seconds
timers:  115 ; remaining: 0.1 seconds
timers:  101 ; remaining: 0.1 seconds
timers:   88 ; remaining: 0.0 seconds
timers:  -1 ; remaining: 0.0 seconds
</code>
So the first timers are off by about 0.2 seconds but it's more accurate once the initial error is taken into account (the number of alarms is just <code>N - len(delays)</code>).
If I increase the amount
