import signal
# Test signal.setitimer()

def setitimer_handler(signum, frame):
    print('sigalarm received - {}'.format(signum))
    signal.signal(signal.SIGALRM, signal.SIG_IGN)

signal.signal(signal.SIGALRM, setitimer_handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
print('Waiting for signal...')
signal.pause()

print('Done')
