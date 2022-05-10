import signal
# Test signal.setitimer()
def set_timer(signum):
    print("Signal Number: %d" % signum)
    signal.setitimer(signal.ITIMER_REAL, 1.0)

signal.signal(signal.SIGALRM, set_timer)
signal.setitimer(signal.ITIMER_REAL, 1.0)

while True:
    # This is the main process
    print("Doing work...")
    time.sleep(0.5)
