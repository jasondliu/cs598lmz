import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        print(timeit.default_timer() - timeit.default_timer()) # zero
        sys.exit(0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

while True:  # Busy loop
    pass
</code>


A:

In general, you can't make the open your question just asked with any precision. On MS-Windows, you can use the <code>GetTickCount()</code> function to get the time in milliseconds, but that isn't precise to the microsecond. On Linux and MacOS X, you can get the <code>clock_gettime</code> function to get a number of nanoseconds resolution, but that too will be limited.
You'll need to measure how much error you get from each function and adjust your expectations accordingly.

