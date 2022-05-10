import signal
# Test signal.setitimer(signal.ITIMER_VIRTUAL, howlong, 0)
# and signal.setitimer(signal.ITIMER_PROF, howlong, 0)
PROFFLAG = 1 << 16

def handler(signum, frame):
    now = time.time()
