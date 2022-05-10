import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(), 0)
        print('woo')
        print(delays)
    else:
        print('boo')
        signal.setitimer(signal.ITIMER_REAL, 0, 0)

signal.signal(signal.SIGALRM, handler)
handler()

while delays:
    time.sleep(1)
</code>
But I get this error:
<code>Traceback (most recent call last):
  File "main.py", line 15, in &lt;module&gt;
    signal.signal(signal.SIGALRM, handler)
ValueError: signal only works in main thread
</code>
Searching around I came to the conclusion that this was because I was running this script in a virtual environment, which I guess is a subprocess. So I tried to run it outside of the virtual environment, but I got the same error.
What am I doing wrong, and how can I set these timers?
The reason I want to do this is that I am trying to write a script that tracks
