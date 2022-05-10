import signal
# Test signal.setitimer(signal.ITIMER_VIRTUAL)
# Test signal.setitimer(signal.ITIMER_PROF)

def handler(signum, frame):
    print(signum, 'in handler')

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1, 0)

time.sleep(4)

signal.setitimer(signal.ITIMER_REAL, 1, 0)

time.sleep(20)
print('Done')
