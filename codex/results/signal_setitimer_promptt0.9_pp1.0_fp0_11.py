import signal
# Test signal.setitimer
def handler(signum, frame):
    print('Signal hander called with signal', signum)
    # time.sleep(2)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1, 0.5)

while True:
    print('main thread')
    time.sleep(1)
