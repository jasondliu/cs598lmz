import signal
# Test signal.setitimer()
def setitimer_test(signum, frame):
    print("setitimer_test")
    signal.setitimer(signal.ITIMER_REAL, 0.5)

signal.signal(signal.SIGALRM, setitimer_test)
signal.setitimer(signal.ITIMER_REAL, 0.5)

while True:
    time.sleep(1)
    print("main")
