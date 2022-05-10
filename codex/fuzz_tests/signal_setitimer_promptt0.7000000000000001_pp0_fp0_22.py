import signal
# Test signal.setitimer() and signal.getitimer()

def alarm_handler(signum, frame):
    print('Got alarm')

signal.signal(signal.SIGALRM, alarm_handler)

signal.setitimer(signal.ITIMER_REAL, 3)
print(signal.getitimer(signal.ITIMER_REAL))
time.sleep(1)
print(signal.getitimer(signal.ITIMER_REAL))
time.sleep(1)
print(signal.getitimer(signal.ITIMER_REAL))
signal.setitimer(signal.ITIMER_REAL, 0)
print(signal.getitimer(signal.ITIMER_REAL))
time.sleep(2)
print(signal.getitimer(signal.ITIMER_REAL))
