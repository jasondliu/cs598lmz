import signal
# Test signal.setitimer and signal.getitimer

def handler(signum, frame):
    print('Alarm', signum)

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

for i in range(4):
    time.sleep(0.5)

signal.setitimer(signal.ITIMER_REAL, 0)

signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)

for i in range(4):
    time.sleep(0.5)

signal.setitimer(signal.ITIMER_PROF, 0)

signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.1)

for i in range(4):
    time.sleep(0.5)

signal.setitimer(signal.ITIMER_VIRTUAL, 0)
