import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    if not delays:
        raise KeyboardInterrupt

# Trace the ITIMER_REAL signal.
signal.signal(signal.SIGALRM, handler)

# Set the alarm clock for the first delay.
signal.setitimer(signal.ITIMER_REAL, delays.pop())

try:
    while True:
        pass
except KeyboardInterrupt:
    # Reset the signal handler to its default.
    signal.signal(signal.SIGALRM, signal.SIG_DFL)

# Set the alarm clock for 0 seconds, and wake up this process so we can
# safely check `sys.getitimer(sys.ITIMER_REAL)` without the possibility
# of another alarm clock interrupt waking us up before we're done.
signal.setitimer(signal.ITIMER_REAL, 0)
sys.stdout.write("\x07")

print("Ran {} alarm clocks.".format(N))
print("The final alarm clock had
