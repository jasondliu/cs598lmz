import signal
# Test signal.setitimer and signal.setitimer
def handler(signum, frame):
    print('I received signal', signum)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5)

print('Before:', time.time())
time.sleep(5)
