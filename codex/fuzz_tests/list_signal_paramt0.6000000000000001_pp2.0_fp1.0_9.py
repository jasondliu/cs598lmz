import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(), 0)
        print("Interrupted")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(), 0)

while delays:
    pass

print("Done")
</code>
The <code>while delays</code> loop is a busy wait.  A more idiomatic way would be to use <code>select.select</code> on an empty file descriptor list, and <code>signal.setitimer</code> to set the timeout.  That way the interpreter is not wasting CPU.

