import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

while delays:
    signal.pause()
</code>
This is a very simple program that does nothing except to set the timer for N times. I would expect it to take about 20 seconds to run. However, it takes about 2 minutes to run.
I found that the timer is not precise. If I run the program many times, I will get different results. Sometimes it takes as long as 3 minutes.
I am using Python 3.7.1 on Ubuntu 18.04.1.


A:

It's not that precise because it depends on your system's clock interrupt frequency.
<code>$ cat /proc/interrupts | grep -i rtc
  8:  2328  0   IO-APIC-edge      rtc0
$ cat /proc/
