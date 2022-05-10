import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
        print('   ', len(delays))
    else:
        print('done')
        signal.signal(signal.SIGALRM, signal.SIG_DFL)

signal.signal(signal.SIGALRM, handler)
handler()

while delays:
    a = sum(x for x in range(10000))

print(a)
</code>
Works on my machine:
<code>   9999
   9998
   9997
   9996
...
</code>

