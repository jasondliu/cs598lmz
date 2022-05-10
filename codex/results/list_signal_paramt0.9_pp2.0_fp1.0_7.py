import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while delays:
    signal.pause()
</code>
This is the console output:
<code>$ sudo ./itimer_test.py                                                                                                                                                                                                                                                                                                
[sudo] password for user: 
Traceback (most recent call last):
  File "./itimer_test.py", line 15, in &lt;module&gt;
    signal.setitimer(signal.ITIMER_REAL, delays.pop())
signal.error: [Errno 22] Invalid argument
</code>
Python v3.5.1 (Anaconda 4.0.0 64-bit)
Ubuntu v16.04
Additional info requested in comment:
<code>group@vbox:/media/group/DATA2/home/group/src/python/py-itimer$ uname
