import signal
# Test signal.setitimer()

# setitimer(which, seconds, interval=0)
# which: ITIMER_REAL, ITIMER_VIRTUAL, ITIMER_PROF
# seconds: how many seconds to wait before sending the signal
# interval: how many seconds to wait before sending the signal again

def handler(signum, frame):
    print("\rReceived SIGALRM")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 2, 1)

while True:
    pass

# ITIMER_REAL: decrements in real time, and delivers SIGALRM upon expiration
# ITIMER_VIRTUAL: decrements only when the process is executing, and delivers SIGVTALRM upon expiration
# ITIMER_PROF: decrements both when the process is executing and when the system is executing on behalf of the process.
#              Delivers SIGPROF upon expiration
#
# The remaining time in the timer is accessible via the getsitimer() function
#
# setitimer() returns the
