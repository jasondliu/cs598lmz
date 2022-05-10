import signal
# Test signal.setitimer
def handler(signum, frame):
    print("Signal", signum)
    #signal.setitimer(signal.ITIMER_VIRTUAL, 2)
    signal.setitimer(signal.ITIMER_REAL, 2)
    #signal.setitimer(signal.ITIMER_PROF, 2)

signal.signal(signal.SIGALRM, handler)
#signal.setitimer(signal.ITIMER_VIRTUAL, 1)
signal.setitimer(signal.ITIMER_REAL, 1)
#signal.setitimer(signal.ITIMER_PROF, 1)

while True:
    pass
