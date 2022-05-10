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

print(time.time())
while delays:
    signal.pause()
print(time.time())
</code>
and the results are:
<code>1468679925.0
1468679925.001426
1468679925.047565
1468679925.071506
1468679925.071613
1468679925.071721
1468679925.071828
1468679925.071935
1468679925.072042
1468679925.072149
1468679925.072257
1468679925.072364
1468679925.072471
1468679925.
