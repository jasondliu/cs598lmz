import signal
# Test signal.setitimer() with SIGALRM.
signal.setitimer(signal.ITIMER_REAL, 0.005, 0)
signal.signal(signal.SIGALRM, lambda signum, itimerval: setattr(signal, 'alarm_received', True))
signal.alarm_received = False
for i in xrange(5000):
    if signal.alarm_received:
        print 'ITIMER_REAL expired'
        sys.exit(0)
print 'ITIMER_REAL not expired'
sys.exit(1)
