import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
        #print('t = ', round(time.time(), 3))

    else:
        print('--------------------------')
        print('done')

signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
signal.signal(signal.SIGALRM, handler)

while delays:
    pass

</code>
The code above triggers SIGALRM "successively at the time intervals specified by the it_value field of <code>new_setting</code> and if the it_interval field of <code>new_setting</code> is nonzero, also successively at the time intervals specified by the it_interval field" (source), but, as you see, it's hard to achieve an exact interval and the accuracy gets lower for longer intervals.
<code>signal.setitimer</code> has two parameters: how long to wait until triggering the signal, and how often to trigger it in the future. I want to trigger the signal only once, so I set the second to 0.
The
