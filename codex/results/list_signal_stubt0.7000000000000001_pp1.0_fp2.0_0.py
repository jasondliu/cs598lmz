import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while delays:
    signal.pause()
</code>
I added a print statement to the signal handler and ran it on my machine (Mac OS X 10.6.4, Intel Core 2 Duo, Python 2.6.4). The delays are not uniform, although they're all close to 1.5 ms.
<code>&gt;&gt;&gt; ./timer.py
0.000327682495117
0.000277996063232
0.00037693977356
0.000283006668091
0.000298023223877
0.00031495098877
0.000290870666504
0.000282049179077
0.000240087509155
0.000267963409424
0.00025200843811

