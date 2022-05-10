import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

# Test signal.getitimer()
print 'sig_handler() : sig_handler.itimer_value', signal.getitimer(signal.ITIMER_REAL)
print 'sig_handler() : sig_handler.itimer_interval', signal.getitimer(signal.ITIMER_REAL)

def sig_handler(signum, frame):
	print 'sig_handler() : sig_handler.itimer_value', signal.getitimer(signal.ITIMER_REAL)
	print 'sig_handler() : sig_handler.itimer_interval', signal.getitimer(signal.ITIMER_REAL)
	print 'sig_handler() : sig_handler.itimer_value', signal.getitimer(signal.ITIMER_REAL)
	print 'sig_handler() : sig_handler.itimer_interval', signal.getitimer(signal.ITIMER
