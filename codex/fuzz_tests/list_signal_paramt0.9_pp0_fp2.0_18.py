import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop() / 1000, 0)
        print('Save data')
    else:
        print('This is the last run')

signal.setitimer(signal.ITIMER_REAL, delays.pop() / 1000, 0)
signal.signal(signal.SIGALRM, handler)

while 1:
    try:
        time.sleep(8e16)
    except:
        pass
</code>
The probelm is, that the function handler() is called every 15 seconds, no matter how the delay was set. So, I always see the output
<code>Save data
Save data
Save data
Save data
...
</code>
Is there a way to do that, and what am I doing wrong?


A:

It will sleep for 15 seconds (actual time will vary):
<code>time.sleep(8e16)
</code>
<code>time.sleep</code> takes <code>seconds</code> as argument, and <code>8e16</code> (or <code>
