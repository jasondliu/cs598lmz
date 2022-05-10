import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        sys.exit(1)
    return

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

# Set up a socket pair to send messages to the "main thread".
#
# This socket pair is non-blocking.  The "main thread" will get
# an EAGAIN error if it attempts to read before there is something
# available to read.

sock1, sock2 = socket.socketpair()
sock1.setblocking(0)
#sock1.setblocking(1)
sock2.setblocking(0)
#sock2.setblocking(1)

# Create a lock to synchronize the main thread with the signal handler.
#
# In the main thread, the lock will be acquired, then the read syscall
# will be issued.  In the signal handler, the lock will be released,
# which will wake up the main thread.

