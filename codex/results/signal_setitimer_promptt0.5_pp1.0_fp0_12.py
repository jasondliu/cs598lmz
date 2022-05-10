import signal
# Test signal.setitimer() and signal.getitimer()

def alarm_handler(signum, frame):
    print('Got SIGALRM')
    print('setitimer(ITIMER_REAL, 0.0)')
    signal.setitimer(signal.ITIMER_REAL, 0.0)

signal.signal(signal.SIGALRM, alarm_handler)
print('setitimer(ITIMER_REAL, 0.1)')
signal.setitimer(signal.ITIMER_REAL, 0.1)
print('getitimer(ITIMER_REAL) =', signal.getitimer(signal.ITIMER_REAL))
print('Sleeping...')
time.sleep(1)
print('getitimer(ITIMER_REAL) =', signal.getitimer(signal.ITIMER_REAL))
print('Done.')
