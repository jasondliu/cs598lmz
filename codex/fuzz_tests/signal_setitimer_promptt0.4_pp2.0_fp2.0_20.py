import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.1)
print 'Alarm starting'
signal.pause()
print 'Alarm ended'
