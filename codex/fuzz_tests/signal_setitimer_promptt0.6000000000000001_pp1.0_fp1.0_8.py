import signal
# Test signal.setitimer()

def handler(signum, frame):
    print('Alarm', signum, frame)
    signal.setitimer(signal.ITIMER_REAL, 1)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1)

while True:
    pass

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
