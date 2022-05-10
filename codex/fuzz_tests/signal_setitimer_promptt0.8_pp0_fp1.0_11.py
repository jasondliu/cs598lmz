import signal
# Test signal.setitimer()

def alarm_handler(signum, frame):
    print 'Alarm!'

signal.signal(signal.SIGALRM, alarm_handler)

signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

try:
    while True:
        print 'Waiting...'
        time.sleep(1)
except KeyboardInterrupt:
    # Disable the alarm
    signal.setitimer(signal.ITIMER_REAL, 0)
    print 'Disabled the alarm'
