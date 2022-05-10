import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        sys.exit(0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

# block until first signal is sent
while delays:
    pass

# do computationally expensive task
for i in xrange(10000000):
    pass
</code>
The problem is that this code is not portable, because it uses <code>signal.setitimer</code>, which is a Unix API.  I would like to write this code in a portable manner.  I know that I can use <code>signal.set_wakeup_fd</code> which is a portable API (the documentation says it is available on Windows, Mac and Linux), but it is not clear to me how to use this API to achieve the same effect.  Specifically, the documentation says:
<blockquote>
<p>If the signal is generated, the operating system wakes up the process
  by writing a byte to the wakeup fd. If the byte is read, the process
  remains awake. To avoid a
