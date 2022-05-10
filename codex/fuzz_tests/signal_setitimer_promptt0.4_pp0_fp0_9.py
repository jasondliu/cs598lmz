import signal
# Test signal.setitimer()
#
# This program tests signal.setitimer() by setting up a SIGALRM handler
# and a SIGPROF handler.  The SIGALRM handler prints a message, and
# the SIGPROF handler increments a counter.  The test passes if the
# counter is incremented every second.

import signal

# The signal handler for SIGALRM
def alarm_handler(signum, frame):
    print "SIGALRM:", signum, frame

# The signal handler for SIGPROF
def prof_handler(signum, frame):
    global counter
    counter = counter + 1
    print "SIGPROF:", signum, frame, counter

# The main test program
def main():
    global counter
    print "Setting up signal handlers"
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.signal(signal.SIGPROF, prof_handler)
    print "Setting itimer"
    signal.setitimer(signal.ITIMER_PROF, 1.0, 1.0)
    print "S
