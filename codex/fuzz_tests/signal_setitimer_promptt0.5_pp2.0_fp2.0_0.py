import signal
# Test signal.setitimer()

def handler(num, frame):
    print 'Signal handler called with signal', num

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL,0.1)
while True:
    pass
