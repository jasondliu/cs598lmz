import signal
# Test signal.setitimer
# This program is intended to be run from the command line with an argument

def handler(signum, frame):
    print >> sys.stderr, "Timeout!"

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, float(sys.argv[1]))
raw_input()
print "Submit!"
