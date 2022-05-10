import signal
# Test signal.setitimer and signal.alarm for setting (real) time
# alarms, and signal.setitimer and signal.settimer for setting
# CPU-time alarms.
signal.alarm(10)
signal.setitimer(signal.ITIMER_REAL,1,1)
signal.setitimer(signal.ITIMER_VIRTUAL,1,1)
signal.setitimer(signal.ITIMER_PROF,1,1)
print 'sleeping'
signal.pause()
print 'dead'
