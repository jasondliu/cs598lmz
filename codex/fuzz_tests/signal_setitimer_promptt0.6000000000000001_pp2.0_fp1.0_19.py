import signal
# Test signal.setitimer()
def alarm_handler(signum, frame):
    print 'Alarm:', time.strftime('%X')

signal.signal(signal.SIGALRM, alarm_handler)

print 'Set:', time.strftime('%X')
signal.setitimer(signal.ITIMER_REAL, 2, 1)

while True:
    print 'Loop:', time.strftime('%X')
    time.sleep(0.5)
