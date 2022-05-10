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
I would like to ask: what is the best way to implement time precise delay in python, keeping in mind the following:

best performance
the delay does not have to be precise, but the imprecision should be small and uniform.

My options are:

Using signals. I am not sure how accurate the timer is.
Using either <code>asyncio</code> or <code>threading</code>. I am not sure how precise the sleep is.
Using <code>ctypes</code> and call nanosleep in c.



A:

The best way to get high resolution timings in python is to use the timeit module.
You can use this module to test how precise different methods of sleeping are.
Example:
<code>import timeit
def timeit_test():

