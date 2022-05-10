import signal
# Test signal.setitimer()

def alarm_handler(signum, frame):
    print('Alarm!')

signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 1, 0.5)

for i in range(5):
    print('Sleeping...')
    time.sleep(1)
