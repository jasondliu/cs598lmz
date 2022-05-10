import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        return
    raise SystemExit

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())
#signal.siginterrupt(signal.SIGALRM, False)

start = time.time()

while delays:
    time.sleep(1000)

end = time.time()

print(end - start)
</code>
This version produces these update rates:
<code>~$ for i in `seq 1 10`; do python3 sigalrm.py; done
0.09997117137908936
0.1000210666656494
0.09987785816192627
0.10016653537750244
0.0999055290222168
0.10008454322814941
0.09996414184570312
0.10003888607025146
0.09998002052307129
0.0999512
