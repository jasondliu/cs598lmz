import signal
# Test signal.setitimer(signal.ITIMER_PROF, 0.5);
# and exit after ~5 seconds...

def handler(signum, frame):
    print("signum: ", signum, " frame: ", frame)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_PROF, 0.5);
time.sleep(5)
signal.alarm(0)
