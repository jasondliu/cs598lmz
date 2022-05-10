import signal
# Test signal.setitimer()

# First, use a handler that raises an exception.
# This can't be handled by the main program, so
# the whole process will die.

def handler(signum, frame):
    raise RuntimeError, "got signal %d" % signum

for sig in 1, 2, 3, 15:
    signal.signal(sig, handler)
    signal.setitimer(signal.ITIMER_REAL, 1.0, 0.0)
    print "Sleeping for 2 seconds"
    time.sleep(2)
    print "Done sleeping"

# Next, use a handler that just sets a flag.

got_alarm = 0
def handler(signum, frame):
    global got_alarm
    got_alarm = 1

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1.0, 0.0)
print "Sleeping for 2 seconds"
time.sleep(2)
print "Done sleeping"
if not got_al
