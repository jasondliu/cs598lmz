import signal
# Test signal.setitimer() and signal.getitimer()

def alarm_handler(signum, frame):
    print('Got alarm')

signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)
print('Sleeping')
signal.pause()
print('Done')
