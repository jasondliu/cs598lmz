import signal
# Test signal.setitimer()

def alarm_handler(signum, frame):
    print('Alarm!')

signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

while True:
    signal.pause()

# Test signal.setitimer()

def alarm_handler(signum, frame):
    print('Alarm!')

signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

while True:
    signal.pause()

# Test signal.setitimer()

def alarm_handler(signum, frame):
    print('Alarm!')

signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

while True:
    signal.pause()

# Test
