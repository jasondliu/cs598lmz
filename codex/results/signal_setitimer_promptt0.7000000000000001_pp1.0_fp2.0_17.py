import signal
# Test signal.setitimer with interval and sigalarm

def alarm_handler(signo, frame):
    print('Alarm', signo, frame)

signal.signal(signal.SIGALRM, alarm_handler)

# inteval is 2
signal.setitimer(signal.ITIMER_REAL, 2, 0)

while True:
    print('Tick')
    time.sleep(1)
