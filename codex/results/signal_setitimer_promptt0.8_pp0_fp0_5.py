import signal
# Test signal.setitimer() and signal.getitimer()
def alarm_handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("I'm bored")

old_handler = signal.signal(signal.SIGALRM, alarm_handler)

signal.setitimer(signal.ITIMER_REAL, 0.25)
print('About to sleep')
signal.setitimer(signal.ITIMER_REAL, 0)
time.sleep(0.1)
try:
    print('About to sleep')
    time.sleep(0.5)
except OSError:
    print('Got OSError')
signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, old_handler)
time.sleep(1)
