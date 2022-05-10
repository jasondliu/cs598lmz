import signal
# Test signal.setitimer
def handler(signum, frame):
    print 'Received signal: %s' % signum

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 2)

print 'Start...'

# Do something
time.sleep(100)
