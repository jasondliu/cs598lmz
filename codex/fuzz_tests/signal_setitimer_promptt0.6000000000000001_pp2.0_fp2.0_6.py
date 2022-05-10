import signal
# Test signal.setitimer
# This test is Linux specific
signals_arrived = []
def handler(signum, frame):
    signals_arrived.append(signum)
    signal.setitimer(signal.ITIMER_REAL, 0.2)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.2)
time.sleep(1)
signal.setitimer(signal.ITIMER_REAL, 0)
if signals_arrived != [signal.SIGALRM] * 5:
    print("Test failed, signals arrived:", signals_arrived)
else:
    print("Test passed")
