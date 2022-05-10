import signal
# Test signal.setitimer

def alarm(signum, frame):
    raise TimeoutError

signal.signal(signal.SIGALRM, alarm)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
try:
    while True:
        pass
except TimeoutError:
    print('Time is out')
