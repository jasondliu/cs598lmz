import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        print("all delays processed")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

try:
    while True:
        print("waiting for next alarm")
        signal.pause()
except KeyboardInterrupt:
    print("interrupted")
</code>
Note that there is a small but non-zero chance that the kernel will miss a signal, so the pauses may be longer than you expect. You can mitigate this by setting the interval to a smaller value, but then you'll be spending more time in the signal handler. In any case, you're probably better off using a thread to do the work and then use the <code>signal</code> module to send the thread a <code>SIGALRM</code> signal instead of trying to use the <code>signal</code> module in the thread itself.

