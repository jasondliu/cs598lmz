import signal
# Test signal.setitimer

def handler(signum, frame):
    print()
    print('Signal handler called with signal', signum)
    raise OSError("I'm done")

signal.signal(signal.SIGALRM, handler)

# Defaults to real time
signal.setitimer(signal.ITIMER_REAL, 1)

while True:
    pass
