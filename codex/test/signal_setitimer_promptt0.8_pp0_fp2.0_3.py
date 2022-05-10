import signal
# Test signal.setitimer()
def signal_handler(signum, frame):
    print('Received signal %s' % signum)

signal.signal(signal.SIGALRM, signal_handler)
# signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
while True: pass
# Here we set up a simple signal handler, and then set up a timer to
# send a SIGALRM signal every 0.1 seconds.
