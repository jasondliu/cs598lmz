import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.setitimer(signal.ITIMER_REAL, delays.pop())
signal.signal(signal.SIGALRM, handler)

while delays:
    pass
</code>
The code above is the simplest example of code that works fine on my machine.
My questions are:

Is there a better way to do this?
Is there a way to do this with a single thread?
Is there a way to do this on Windows?
Is there a way to do this without spawning a process?

Please note that I am not interested in parallelism. I am trying to mimic a real-time system that needs to run a number of tasks in a timely manner. The tasks do not depend on one another and can be run in any order.


A:

<blockquote>
<ol>
<li>Is there a better way to do this?</li>
</ol>
</blockquote>
Yes, you can use the <code>threading</code> module, which has a <code>Timer</code> class that can be used for this. It's not real-time,
