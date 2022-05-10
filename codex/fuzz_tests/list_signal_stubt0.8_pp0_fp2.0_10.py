import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
# Register handler for SIGALRM
signal.signal(signal.SIGALRM, handler)

# Initialize first alarm
signal.setitimer(signal.ITIMER_REAL, delays.pop())

# When we reach here, we are waiting for the first SIGALRM.
# Usually, we would do some processing here (e.g. open a file,
# do the read, whatever). Instead we just sleep for a long
# time.
time.sleep(300)
</code>

