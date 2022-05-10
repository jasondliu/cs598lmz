import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_VIRTUAL, delays.pop(0))
        print(signum, frame)

signal.signal(signal.SIGVTALRM, handler)
signal.setitimer(signal.ITIMER_VIRTUAL, delays.pop(0))

while delays:
    sleep(0.01)
</code>
Is that because I'm calculating delays with <code>1e-6 + random.random() * 2e-5</code> and that's not enough precision?
I was expecting that the handler function would be called with a frequency of at least 100 Hz if I use <code>sleep(0.01)</code>


A:

This is not the way to go about getting high precision timers.
<code>sleep</code> is implemented using <code>select</code> or <code>poll</code>, which are in turn implemented using a system call which returns when the next timeout expires.
This has the effect of coalescing all the timers into the next expiration time. In your case, the system call would return after 1 second or at most a few milliseconds if there
