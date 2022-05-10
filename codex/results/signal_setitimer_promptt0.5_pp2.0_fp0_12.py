import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

print 'Sleeping'
time.sleep(5)
print 'Exiting'
