import signal
# Test signal.setitimer()
def handler_setitimer(signum, frame):
	print 'Received signal: ', signum

signal.signal(signal.SIGALRM, handler_setitimer)
signal.setitimer(signal.ITIMER_REAL, 2, 0)
pause()
# Test signal.setitimer()
# Test signal.setitimer()
def handler_setitimer(signum, frame):
	print 'Received signal: ', signum

signal.signal(signal.SIGALRM, handler_setitimer)
signal.setitimer(signal.ITIMER_REAL, 2, 0)
pause()
# Test signal.setitimer()
# Test signal.setitimer()
def handler_setitimer(signum, frame):
	print 'Received signal: ', signum

signal.signal(signal.SIGALRM, handler_setitimer)
signal.setitimer(signal.ITIMER_REAL, 2, 0)
pause()
# Test signal.set
