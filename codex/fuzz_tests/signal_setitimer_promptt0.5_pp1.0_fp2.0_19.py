import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

def handler(signum, frame):
    print('Alarm!')

signal.signal(signal.SIGALRM, handler)

# signal.setitimer(signal.ITIMER_REAL, 5)
# signal.alarm(5)
# signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
# signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
# signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
# signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

# signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
# signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
# signal.setit
