import signal
# Test signal.setitimer()
def handler(signum, s):
	print '\nHandler called:', signum, s
	#block/unblock signal
	#signal.setitimer(signal.ITIMER_REAL, 2)

signal.signal(signal.SIGALRM, handler)

#if arg is 0, timer is disabled
signal.setitimer(signal.ITIMER_REAL, 2)

#do time intensive process here
c = 0
for i in range(1, 100000):
	for j in range(1, 1000000):
		c = c+ i*j
	
#cancel timer - 0
signal.setitimer(signal.ITIMER_REAL, 0)
