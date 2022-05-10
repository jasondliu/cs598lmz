import signal
# Test signal.setitimer() (for Solaris)
import signal

def signal_handler(signum, frame):
    print "signum:%d" % signum
    print "frame:%s" % frame

signal.signal(signal.SIGALRM, signal_handler)
signal.setitimer(signal.ITIMER_REAL, 0.001)

# b/c this is a testsuite, it has to wait a little before
# the signal gets called.
time.sleep(1)

# SIGALRM is the only signal that can be caught 
# (not SIGKILL, SIGSTOP, SIGBUS, ...)
signal.kill(pid, signal.SIGALRM)
time.sleep(1)

# Run the same test with ITIMER_VIRTUAL 
# (for Linux/FreeBSD)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.001)
time.sleep(1)
signal.kill(pid, signal.SIGVTALRM)
time.sleep(1)

#
