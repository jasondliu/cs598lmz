import signal
# Test signal.setitimer() for alarm()

signal.alarm(2)

def handler(signum, frame):
    print('Alarm')
    raise SystemExit

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 1)

time.sleep(3)

print('Done')
