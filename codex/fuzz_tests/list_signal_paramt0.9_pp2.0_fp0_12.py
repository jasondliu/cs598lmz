import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        sys.exit(0)

signal.signal(signal.SIGALRM, handler)

handler()
signal.pause()
</code>
You can try it like this:
<code>$ python t.py | head -100 | sort -k3,3n | more
Tue Dec  3 12:47:21 2013          1 5.0823405e-05
Tue Dec  3 12:47:21 2013          2 5.0824454e-05
Tue Dec  3 12:47:21 2013          3 6.0820617e-05
Tue Dec  3 12:47:21 2013          4 6.0821883e-05
Tue Dec  3 12:47:21 2013          5 7.0818893e-05
Tue Dec  3 12:47:21 2013          6 7.0819049e-05
Tue Dec  3 12:47:21 2013          7 7.0821593e-05
Tue Dec  3 12:47:21 2013          8 8.0819477e
