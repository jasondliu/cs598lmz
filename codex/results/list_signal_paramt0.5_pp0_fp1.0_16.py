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
print("starting")
while delays:
    signal.pause()
    sys.stdout.write(".")
    sys.stdout.flush()
sys.stdout.write("\n")
</code>
The output of this is:
<code>starting
....................................................................................................
</code>

