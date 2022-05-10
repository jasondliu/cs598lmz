import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        foo()

def foo():
    print("Caught a timer signal!")

# Let's set up the timer
signal.signal(signal.SIGALRM, handler)

# Install the guard. This should make sure that we catch the
# timer signals, even if the handler is swapped out by the
# profiler or tracer.
signal.siginterrupt(signal.SIGALRM, False)

# Register the first timer to go off in one second
signal.setitimer(signal.ITIMER_REAL, 1.0)

# Run in a busy loop...
i = 0
while delays:
    i += 1

print("No more timer sigals, Exiting after {} 
