import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

# Call handler() on SIGALRM
signal.signal(signal.SIGALRM, handler)

# Schedule the first alarm for 1 second from now
signal.setitimer(signal.ITIMER_REAL, 1)

# Do some busy work
for i in range(1, 5):
    print 'Working', i
    time.sleep(1)

# Schedule the second alarm for 1 second after the first alarm
signal.setitimer(signal.ITIMER_REAL, 1)

# Do some more busy work
for i in range(5, 10):
    print 'Working', i
    time.sleep(1)
