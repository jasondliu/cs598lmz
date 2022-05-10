import signal
# Test signal.setitimer() and signal.getitimer()

def handler(signum, frame):
    print('Signal handler called with signal', signum)

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 1.0)
print('Sleeping')
time.sleep(5)
print('Exiting')
