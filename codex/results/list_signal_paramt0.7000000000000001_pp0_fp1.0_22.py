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

You may want to run the code with a higher priority to reduce jitter, e.g.
<code>sudo ionice -c 1 -n -1 nice -n -20 python3 timer.py
</code>
Or on Python 2.7.9+:
<code>python2.7 -m subprocess --nice=19 python timer.py
</code>
Note that on Linux, you will probably have to raise your <code>max_user_watches</code> limit:
<code>sudo sh -c 'echo 1000000 &gt; /proc/sys/fs/inotify/max_user_watches'
</code>

