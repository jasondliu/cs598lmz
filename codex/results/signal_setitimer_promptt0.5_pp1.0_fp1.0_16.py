import signal
# Test signal.setitimer()
def handler(signum, frame):
    print("Received signal", signum)
    signal.setitimer(signal.ITIMER_REAL, 0.5)
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5)

time.sleep(2)

# Test signal.setitimer()
def handler(signum, frame):
    print("Received signal", signum)
    signal.setitimer(signal.ITIMER_VIRTUAL, 0.5)
signal.signal(signal.SIGVTALRM, handler)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.5)

time.sleep(2)

# Test signal.setitimer()
def handler(signum, frame):
    print("Received signal", signum)
    signal.setitimer(signal.ITIMER_PROF, 0.5)
signal.signal(signal.SIG
