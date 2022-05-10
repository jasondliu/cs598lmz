import signal
# Test signal.setitimer
print 'Set ITIMER_REAL.'
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
time.sleep(0.2)
print 'Set ITIMER_PROF.'
signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)
time.sleep(0.2)
print 'Set ITIMER_VIRTUAL.'
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.1)
time.sleep(0.2)
print 'Done'

# Test signal.getsignal
print 'Get SIGINT handler', signal.getsignal(signal.SIGINT)
print 'Get SIGTERM handler', signal.getsignal(signal.SIGTERM)

# Test siginterrupt
print 'Set siginterrupt'
signal.siginterrupt(signal.SIGINT, 1)

# Test signal.signal
def handler(signum, frame):
	print 'Handler'
	
