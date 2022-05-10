import signal
# Test signal.setitimer
def setitimer_signal_handler(num, frame):
	print 'tock'

signal.signal(signal.SIGALRM, setitimer_signal_handler)

print 'setitimer:'
for t in [ 0.1, 0.2, 0.3 ]:
	signal.setitimer(signal.ITIMER_REAL, 0.25, t)
for t in [ 0.1, 0.2, 0.3 ]:
	signal.setitimer(signal.ITIMER_REAL, t, 0)
for t in [ 0.1, 0.2, 0.3 ]:
	signal.setitimer(signal.ITIMER_REAL, t, t)

# Test signal.setitimer with timeout
print 'setitimer timeout:'
for t in [ 0.1, 0.2, 0.3 ]:
	signal.setitimer(signal.ITIMER_REAL, t, 0.4)
	try:
		timeout = t
		sign
