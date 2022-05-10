import signal
# Test signal.setitimer()

def alarm_handler(signum, frame):
    print("Received signal", signum)
    signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 1)

while True:
    # do something
    pass
