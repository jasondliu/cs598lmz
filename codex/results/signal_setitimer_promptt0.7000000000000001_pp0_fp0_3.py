import signal
# Test signal.setitimer() and signal.alarm()

def now():
    print('10:00:00')
    return 0

signal.signal(signal.SIGALRM, now)
signal.setitimer(signal.ITIMER_REAL, 10, 0)
signal.alarm(10)
print 'start'
time.sleep(5)
print 'end'
