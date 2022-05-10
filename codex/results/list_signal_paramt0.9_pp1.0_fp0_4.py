import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

while 1:
    try:
        time.sleep(1e-6)
    except IOError:
        pass
</code>
(On Windows platforms you will also need to add <code>SIGBREAK = 0</code> to the import line. And you will also need to change <code>SIGALARM</code> to <code>SIGBREAK</code>. That's because, on Windows, the SIGALRM is used for some internal mechanism and can't be used by your application.)
But note that if you need the signals to be generated more precisely than the CPython interpreter's check-for-signals loop, doing that is going to be a lot more tricky.

