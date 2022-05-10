import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Alarm'
    raise KeyboardInterrupt

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 2)

try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    pass
