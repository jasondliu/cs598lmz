import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Signal handler called with signal", signum)

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 2)

print("Sleeping for 5 seconds")
time.sleep(5)

print("Done")
