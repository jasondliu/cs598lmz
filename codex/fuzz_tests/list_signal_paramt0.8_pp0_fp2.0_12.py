import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0), 0)
    else:
        signal.setitimer(signal.ITIMER_REAL, 0, 0)

signal.setitimer(signal.ITIMER_REAL, 0, 0)
signal.signal(signal.SIGALRM, handler)
handler()
</code>
Here you have a sample execution:
<code>anubhava@dumbo:/tmp$ python foo.py
^C0.000239
0.000198
0.000583
0.000180
0.000014
0.000312
0.000153
0.000106
0.000096
0.000028
0.000048
0.000116
0.000169
^C^C^C^C^C^C^C^C^C^C^C^C^C^C^C^C^C^C^C^C^C^C^C^C^C^C^C^C^C^C^C^C^C^C^C
