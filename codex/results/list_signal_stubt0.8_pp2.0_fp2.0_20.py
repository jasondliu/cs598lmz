import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print('Done')

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while delays:
    time.sleep(1)
</code>
but it is hardly efficient and it is blocking python GIL. So I guess the only solution is to use some C/C++ extension that will create and start a native thread that will do the same job, but I do not want to write it myself.
Any suggestions?
The reason why I need this is that I want to simulate a continuous flow of events with fixed event rate:
<code>1
1
1
</code>
but they are not coming one by one, they are coming in batches.

