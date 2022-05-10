import signal
# Test signal.setitimer() and signal.getitimer().
# Signal handler prints the timer value and resets the timer.
# If the timer expires, "end" is printed and the program exits.

def handler(signum, frame):
    print 'Alarm', signal.getitimer(signal.ITIMER_REAL)
    signal.setitimer(signal.ITIMER_REAL, 1)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1)

while 1:
    signal.pause()
