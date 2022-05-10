import signal
# Test signal.setitimer()
def handler(signum, frame):
    print('Received signal', signum)
    raise OSError('Error')

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.25, 0.25)

# Main code
# signal.alarm(1)
cnt = 0
try:
    while True:
        print('Loop count', cnt)
        cnt += 1
        time.sleep(1)
except OSError:
    print('Caught OSError')
    signal.setitimer(signal.ITIMER_REAL, 0)
    time.sleep(1)
    print('Done')

# signal.setitimer(signal.ITIMER_REAL)

# signal.setitimer(signal.ITIMER_VIRTUAL)
# signal.setitimer(signal.ITIMER_PROF)
