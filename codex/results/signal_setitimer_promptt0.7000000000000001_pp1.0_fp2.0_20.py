import signal
# Test signal.setitimer()
def handler(signum, frame):
	print "goodbye"
	raise SystemExit

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 2)

print "start"

while True:
	time.sleep(0.1)
	pass
