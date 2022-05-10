import signal
# Test signal.setitimer
# Test signal.setitimer with SIGALRM
# Test signal.setitimer with SIGVTALRM
# Test signal.setitimer with SIGPROF

# Test SIGALRM
def alarm_handler(signum, frame):
    print("SIGALRM received")
    signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)
# SIGALRM is received
while True:
    pass

# Test SIGVTALRM
def vtalarm_handler(signum, frame):
    print("SIGVTALRM received")
    signal.setitimer(signal.ITIMER_VIRTUAL, 0)

signal.signal(signal.SIGVTALRM, vtalarm_handler)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1)
# SIGVTALRM is received
while True:
    pass

