import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_VIRTUAL, delays.pop(0))

signal.signal(signal.SIGVTALRM, handler)
handler(None, None)

while delays:
    sleep(1e6)
</code>
This code prints the following output:
<code>user    0m0.268s
sys     0m0.000s
</code>
How is it that the "user" time to finish the script is 0m0.268s when I'm explicitly sleeping for 1000000 seconds?  What am I not understanding about the "user" time in this example?
I'm using Python 2.7.3 on a Mac with OS X 10.8.3, if that helps.


A:

As you can see from <code>/usr/include/sys/time.h</code>, the <code>ITIMER_VIRTUAL</code> timer is decremented only when a process is running in user mode.
So for the most part, your sleep is not consuming CPU time at all. But when your alarm goes off, the handler is consuming CPU time.

