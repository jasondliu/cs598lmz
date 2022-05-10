import signal
# Test signal.setitimer()
#
# This test is derived from test_signal.py, but with the setitimer()
# calls removed.
#
# This test should be run in the background, and then it should be
# killed with SIGALRM.  It should print "ok" before it exits.

def alarm_received(n, stack):
    print 'ok'
    sys.exit(0)

signal.signal(signal.SIGALRM, alarm_received)

# signal.setitimer(signal.ITIMER_REAL, 0.1)

# Don't let Ctrl-C kill us.
signal.signal(signal.SIGINT, signal.SIG_IGN)

# Wait until we get SIGALRM
while 1:
    pass
