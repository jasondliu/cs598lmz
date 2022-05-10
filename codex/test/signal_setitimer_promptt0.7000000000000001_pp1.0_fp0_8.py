import signal
# Test signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)

def start():
    signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)

def stop():
    signal.setitimer(signal.ITIMER_PROF, 0, 0)

