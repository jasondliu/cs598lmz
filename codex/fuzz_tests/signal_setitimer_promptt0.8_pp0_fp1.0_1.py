import signal
# Test signal.setitimer()
def alrm_handler(signum, frame):
    print("Test PASS!")

signal.signal(signal.SIGALRM, alrm_handler)
signal.setitimer(signal.ITIMER_REAL, 0, 0.1)

while True:
    pass
