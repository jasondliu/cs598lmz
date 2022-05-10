import signal
# Test signal.setitimer() and signal.getitimer().

print 'Testing getitimer/setitimer'
for i in [signal.ITIMER_REAL, signal.ITIMER_VIRTUAL, signal.ITIMER_PROF]:
    print ' ', i
    signal.setitimer(i, 1.0)
    for j in range(3):
        time.sleep(0.5)
        print '  ', signal.getitimer(i)
    signal.setitimer(i, 0.0)

# Test signal.alarm().

print 'Testing alarm'
signal.alarm(1)
for i in range(3):
    time.sleep(0.5)
    print ' ', signal.alarm(0)

# Test signal.pause().

print 'Testing pause'
signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.pause()

# Test setting and clearing a signal handler.

print 'Testing signal'
signal.signal(signal.SIGINT, signal.SIG_
