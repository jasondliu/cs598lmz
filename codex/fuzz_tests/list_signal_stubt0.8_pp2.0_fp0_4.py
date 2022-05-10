import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    sys.stdout.write("x")
    sys.stdout.flush()

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

print("Sleeping for 10 seconds...")
time.sleep(10)
</code>
Since your signal handlers are only called at a certain granularity, you might get a few delays around the order of your granularity. But you can tune that however you like.

