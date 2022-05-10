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
Результат в Linux и в BSD примерно одинаковый:
<code>$ python3 ./t.py &amp;
[1] 39739
$ sleep 5; time kill -ALRM 39739

real    0m5.002s
user    0m0.000s
sys     0m0.000s
</code>
Результат в Windows все равно долгий, потому что о
