import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

# Call handler() on SIGALRM
signal.signal(signal.SIGALRM, handler)

# Schedule the first alarm in 1 second
signal.setitimer(signal.ITIMER_REAL, 1)

# Go to sleep, and hope we get woken up by a signal
time.sleep(5)
