import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)
handler()

while delays:
    signal.pause()
</code>
I get inaccurate results even on the smallest delays. This is on a VM with one virtual core:
<code>~/python-playground$ time python3 sigs.py

real    0m1.013s
user    0m0.955s
sys     0m0.017s
~/python-playground$ time python3 sigs.py

real    0m1.011s
user    0m0.957s
sys     0m0.017s
~/python-playground$ time python3 sigs.py

real    0m1.012s
user    0m0.959s
sys     0m0.016s
</code>
The script is CPU bound, but the timing is off.

