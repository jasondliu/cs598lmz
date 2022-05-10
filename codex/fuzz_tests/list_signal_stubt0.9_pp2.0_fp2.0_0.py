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
    time.sleep(10000)
except:
    pass
</code>
This will signal every 1e-6 +- 1e-5 seconds with signal.SIGALRM. However, the 1e-6 +- 1e-5 should be varied more smoothly. For example, 1e-6 +- 1e-5 should vary linearly to 1e-6 +- 4e-5. How should this be achieved ?


A:

Perhaps the following can help. This is just a kind of very naive simulation of what you want. It's not perfect, but maybe you can use the same concept. In this function, the delay is <code>linear</code> in the sense that whether you want a delay of 1 msec or 1 sec, you only need to call <code>my_fixed_delay(.001)</code> or <code>my_fixed_delay(1)</code> respectively.
<code>import time
import random    
