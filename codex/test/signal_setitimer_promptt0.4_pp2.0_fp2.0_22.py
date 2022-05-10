import signal
# Test signal.setitimer() and signal.getitimer()

def alarm_handler(signum, frame):
    print('Got SIGALRM')

signal.signal(signal.SIGALRM, alarm_handler)

signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)

while True:
    print('Tick')
    time.sleep(1)
