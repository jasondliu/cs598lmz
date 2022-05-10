import signal
# Test signal.setitimer()

def alarm_handler(signum, frame):
    print('Got SIGALRM')

signal.signal(signal.SIGALRM, alarm_handler)
# Set the timer to go off in 2 seconds
signal.setitimer(signal.ITIMER_REAL, 2)

print('Before:', signal.getitimer(signal.ITIMER_REAL))
# Do some work
time.sleep(4)
print('After:', signal.getitimer(signal.ITIMER_REAL))
