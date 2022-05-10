import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delay = delays.pop())

    for i in range(100):
        pass


signal.setitimer(signal.ITIMER_REAL, delay = delays.pop())

signal.signal(signal.SIGALRM, handler)

while delays:
    pass

print 'done'
</code>


A:

From the docs:
<blockquote>
<p>A SIGALRM signal is generated only if the timer expires while the process is executing an instruction. If the process is not presently executing an instruction, then the signal will not be generated until the next instruction is executed. This provides a more precise control over the timing of the signal than simply calculating the expiration time and setting a standard alarm.</p>
</blockquote>
The program spends most of its time inside the <code>for</code> loop, so the signal is generated only once every few seconds.
<code>while delays:
    pass
</code>

