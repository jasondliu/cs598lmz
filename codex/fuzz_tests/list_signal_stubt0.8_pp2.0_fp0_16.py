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
With SIGALRM, you can get much higher resolution than time.sleep(), you won't have the Python interpreter delay you with that, and you should be able to get much more accuracy, which you need for your application.
When you call pause(), the system will suspend the current process until it gets a signal. This is similar to what happens, for example, when you call select() with no file descriptors to select on.

